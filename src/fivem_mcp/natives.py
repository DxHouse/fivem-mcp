import bisect
from functools import lru_cache
import json
import os
import re
from collections import defaultdict
from pathlib import Path
from typing import Any
import httpx

NATIVES_URL = "https://runtime.fivem.net/doc/natives.json"
DEFAULT_DATA_DIR = Path(__file__).resolve().parent.parent.parent / "data"
DEFAULT_DATA_FILE = DEFAULT_DATA_DIR / "natives.json"

_TOKEN_RE = re.compile(r"[a-z0-9]+")
_CAMEL_RE = re.compile(r"([a-z])([A-Z])")


def _tokenize(text: str) -> list[str]:
    """Split text into lowercase alphanumeric tokens, handling snake_case and camelCase."""
    if not text:
        return []
    expanded = _CAMEL_RE.sub(r"\1 \2", text).lower()
    return _TOKEN_RE.findall(expanded)


class NativesManager:
    """Manages downloading, inverted indexing, and ultra-fast searching of FiveM natives."""

    def __init__(self, data_file: Path | str | None = None, auto_load: bool = True):
        if data_file:
            self.data_file = Path(data_file)
        else:
            env_path = os.environ.get("FIVEM_NATIVES_PATH")
            self.data_file = Path(env_path) if env_path else DEFAULT_DATA_FILE

        self._loaded = False
        self._all_records: list[dict[str, Any]] = []
        self._formatted_summaries: list[dict[str, Any]] = []
        self._by_name: dict[str, int] = {}
        self._by_hash: dict[str, int] = {}
        self._name_token_index: dict[str, set[int]] = defaultdict(set)
        self._desc_token_index: dict[str, set[int]] = defaultdict(set)
        self._sorted_name_tokens: list[str] = []
        self._namespace_index: dict[str, set[int]] = defaultdict(set)
        self._apiset_index: dict[str, set[int]] = defaultdict(set)

        if auto_load and self.data_file.exists():
            try:
                self.load()
            except Exception:
                pass

    def ensure_data(self) -> Path:
        """Ensure natives.json exists locally; download if missing."""
        if not self.data_file.exists():
            self.data_file.parent.mkdir(parents=True, exist_ok=True)
            print(f"Downloading FiveM natives.json from {NATIVES_URL} to {self.data_file}...")
            with httpx.Client(follow_redirects=True, timeout=30.0) as client:
                resp = client.get(NATIVES_URL)
                resp.raise_for_status()
                self.data_file.write_bytes(resp.content)
            print(f"Saved natives.json ({self.data_file.stat().st_size // 1024} KB)")
        return self.data_file

    def load(self, force_reload: bool = False) -> None:
        """Load and build inverted index in memory."""
        if self._loaded and not force_reload:
            return

        self.ensure_data()
        with open(self.data_file, "r", encoding="utf-8") as f:
            raw_data: dict[str, dict[str, Any]] = json.load(f)

        self._all_records.clear()
        self._formatted_summaries.clear()
        self._by_name.clear()
        self._by_hash.clear()
        self._name_token_index.clear()
        self._desc_token_index.clear()
        self._namespace_index.clear()
        self._apiset_index.clear()

        idx = 0
        for namespace, natives_dict in raw_data.items():
            ns_upper = namespace.upper()
            for hash_key, item in natives_dict.items():
                hash_val = item.get("hash") or hash_key
                name_val = item.get("name") or f"_{hash_val}"
                apiset_val = item.get("apiset", "client").lower()
                desc_val = item.get("description", "")

                record = {
                    **item,
                    "hash": hash_val,
                    "name": name_val,
                    "ns": ns_upper,
                    "apiset": apiset_val,
                }
                self._all_records.append(record)

                # Precompute formatted summary representation
                params_str = ", ".join(
                    f"{p.get('name', 'arg')}: {p.get('type', 'Any')}"
                    for p in item.get("params", [])
                )
                summary_line = desc_val.strip().split("\n")[0] if desc_val else ""
                if len(summary_line) > 120:
                    summary_line = summary_line[:117] + "..."

                self._formatted_summaries.append({
                    "name": name_val,
                    "hash": hash_val,
                    "namespace": ns_upper,
                    "apiset": apiset_val,
                    "signature": f"{name_val}({params_str}) -> {item.get('results', 'void')}",
                    "summary": summary_line,
                })

                # Direct hash mappings
                h_clean = hash_val.lower()
                self._by_hash[h_clean] = idx
                if h_clean.startswith("0x"):
                    self._by_hash[h_clean[2:]] = idx
                else:
                    self._by_hash[f"0x{h_clean}"] = idx

                # Direct name mapping
                name_clean = name_val.lower()
                self._by_name[name_clean] = idx

                # Namespace & apiset index
                self._namespace_index[ns_upper].add(idx)
                self._apiset_index[apiset_val].add(idx)
                if apiset_val == "shared":
                    self._apiset_index["client"].add(idx)
                    self._apiset_index["server"].add(idx)

                # Name tokens indexing
                for tok in _tokenize(name_val):
                    self._name_token_index[tok].add(idx)

                # Description tokens indexing
                for tok in _tokenize(desc_val):
                    self._desc_token_index[tok].add(idx)

                idx += 1

        self._sorted_name_tokens = sorted(self._name_token_index.keys())
        self._loaded = True
        self._search_cached.cache_clear()

    def _get_prefix_token_matches(self, tok: str) -> set[int]:
        """Find record IDs matching prefix token using binary search."""
        matches: set[int] = set()
        pos = bisect.bisect_left(self._sorted_name_tokens, tok)
        while pos < len(self._sorted_name_tokens):
            candidate_tok = self._sorted_name_tokens[pos]
            if not candidate_tok.startswith(tok):
                break
            matches.update(self._name_token_index[candidate_tok])
            pos += 1
        return matches

    @lru_cache(maxsize=1024)
    def _search_cached(
        self,
        query: str,
        namespace: str | None,
        apiset: str,
        limit: int,
    ) -> tuple[int, ...]:
        """Internal cached search returning tuple of matching record indices."""
        q_raw = query.strip()
        if not q_raw:
            return ()

        q_lower = q_raw.lower()
        ns_filter = namespace.strip().upper() if namespace else None
        apiset_filter = apiset.strip().lower() if apiset and apiset != "all" else None

        candidates: set[int] | None = None
        if ns_filter:
            candidates = set(self._namespace_index.get(ns_filter, set()))
            if not candidates:
                return ()

        if apiset_filter and apiset_filter != "all":
            apiset_set = self._apiset_index.get(apiset_filter, set())
            candidates = candidates & apiset_set if candidates is not None else set(apiset_set)
            if not candidates:
                return ()

        # Fast-path: Exact Hash Match
        if q_lower in self._by_hash:
            h_idx = self._by_hash[q_lower]
            if candidates is None or h_idx in candidates:
                return (h_idx,)

        # Fast-path: Exact Name Match
        exact_name_idx = self._by_name.get(q_lower)
        if exact_name_idx is not None and (candidates is None or exact_name_idx in candidates):
            if limit == 1:
                return (exact_name_idx,)

        query_tokens = _tokenize(q_raw)
        if not query_tokens:
            return ()

        # Fast matching with bisect prefix lookup
        token_matches: list[set[int]] = []
        for tok in query_tokens:
            tok_set: set[int] = set()
            if tok in self._name_token_index:
                tok_set.update(self._name_token_index[tok])
            elif len(tok) >= 3:
                tok_set.update(self._get_prefix_token_matches(tok))

            if tok in self._desc_token_index:
                tok_set.update(self._desc_token_index[tok])

            if candidates is not None:
                tok_set &= candidates

            token_matches.append(tok_set)

        token_count_per_candidate: dict[int, int] = defaultdict(int)
        for tok_set in token_matches:
            for c_idx in tok_set:
                token_count_per_candidate[c_idx] += 1

        if not token_count_per_candidate:
            return ()

        num_tokens = len(query_tokens)
        min_required = num_tokens if num_tokens <= 2 else max(2, int(num_tokens * 0.6))

        valid_candidates = {
            c_idx: count
            for c_idx, count in token_count_per_candidate.items()
            if count >= min_required
        }

        if not valid_candidates and num_tokens <= 3:
            max_count = max(token_count_per_candidate.values())
            valid_candidates = {
                c_idx: count
                for c_idx, count in token_count_per_candidate.items()
                if count == max_count
            }

        if not valid_candidates:
            return ()

        scored_list: list[tuple[int, int]] = []
        for c_idx, matched_token_count in valid_candidates.items():
            record = self._all_records[c_idx]
            name_lower = record["name"].lower()
            score = matched_token_count * 100

            if name_lower == q_lower:
                score += 1000
            elif name_lower.startswith(q_lower):
                score += 500
            elif q_lower in name_lower:
                score += 300

            for tok in query_tokens:
                if tok in self._name_token_index and c_idx in self._name_token_index[tok]:
                    score += 50

            scored_list.append((score, c_idx))

        scored_list.sort(key=lambda x: x[0], reverse=True)
        return tuple(c_idx for _, c_idx in scored_list[:limit])

    def search(
        self,
        query: str,
        namespace: str | None = None,
        apiset: str = "all",
        limit: int = 10,
    ) -> list[dict[str, Any]]:
        """Search natives with ultra-fast inverted index and multi-word token scoring."""
        self.load()
        indices = self._search_cached(query, namespace, apiset, limit)
        return [self._formatted_summaries[idx] for idx in indices]

    def get_detail(self, name_or_hash: str) -> dict[str, Any] | None:
        """Get full documentation and details for a native via O(1) dictionary lookup."""
        self.load()
        key = name_or_hash.strip().lower()

        idx = self._by_name.get(key)
        if idx is None:
            idx = self._by_hash.get(key)

        if idx is None:
            return None

        item = self._all_records[idx]
        return {
            "name": item.get("name"),
            "hash": item.get("hash"),
            "namespace": item.get("ns"),
            "apiset": item.get("apiset", "client"),
            "results": item.get("results", "void"),
            "params": item.get("params", []),
            "description": item.get("description", ""),
            "examples": item.get("examples", []),
        }


# Global singleton instance eagerly loaded
natives_manager = NativesManager()
