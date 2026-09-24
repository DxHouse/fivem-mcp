import bisect
from functools import lru_cache
import json
import re
from collections import defaultdict
from pathlib import Path
from typing import Any
import urllib.request

NATIVES_URL = "https://runtime.fivem.net/doc/natives.json"
DATA_FILE = Path(__file__).resolve().parent.parent.parent / "data" / "natives.json"

_TOKEN_RE = re.compile(r"[a-z0-9]+")
_CAMEL_RE = re.compile(r"([a-z])([A-Z])")


def _tokenize(text: str) -> list[str]:
    """Split text into lowercase alphanumeric tokens, handling snake_case and camelCase."""
    if not text:
        return []
    return _TOKEN_RE.findall(_CAMEL_RE.sub(r"\1 \2", text).lower())


class NativesManager:
    """Manages downloading, inverted indexing, and ultra-fast searching of FiveM natives."""

    def __init__(self):
        self._all_records: list[dict[str, Any]] = []
        self._by_name: dict[str, int] = {}
        self._by_hash: dict[str, int] = {}
        self._name_token_index: dict[str, set[int]] = defaultdict(set)
        self._desc_token_index: dict[str, set[int]] = defaultdict(set)
        self._sorted_name_tokens: list[str] = []
        self._namespace_index: dict[str, set[int]] = defaultdict(set)
        self._apiset_index: dict[str, set[int]] = defaultdict(set)
        self.load()

    def ensure_data(self) -> None:
        """Download natives.json if missing."""
        if not DATA_FILE.exists():
            DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
            req = urllib.request.Request(NATIVES_URL, headers={"User-Agent": "FiveM-MCP"})
            with urllib.request.urlopen(req, timeout=30.0) as resp:
                DATA_FILE.write_bytes(resp.read())

    def load(self) -> None:
        """Load and build inverted index in memory."""
        self.ensure_data()
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            raw_data: dict[str, dict[str, Any]] = json.load(f)

        idx = 0
        for namespace, natives_dict in raw_data.items():
            ns_upper = namespace.upper()
            for hash_key, item in natives_dict.items():
                hash_val = item.get("hash") or hash_key
                name_val = item.get("name") or f"_{hash_val}"
                apiset_val = item.get("apiset", "client").lower()
                desc_val = item.get("description", "")

                self._all_records.append({
                    **item,
                    "hash": hash_val,
                    "name": name_val,
                    "ns": ns_upper,
                    "apiset": apiset_val,
                })

                # Normalized mappings
                h_norm = hash_val.lower().removeprefix("0x")
                self._by_hash[h_norm] = idx
                self._by_name[name_val.lower()] = idx

                self._namespace_index[ns_upper].add(idx)
                self._apiset_index[apiset_val].add(idx)
                if apiset_val == "shared":
                    self._apiset_index["client"].add(idx)
                    self._apiset_index["server"].add(idx)

                for tok in _tokenize(name_val):
                    self._name_token_index[tok].add(idx)
                for tok in _tokenize(desc_val):
                    self._desc_token_index[tok].add(idx)

                idx += 1

        self._sorted_name_tokens = sorted(self._name_token_index.keys())

    def _get_prefix_token_matches(self, tok: str) -> set[int]:
        """Find record IDs matching prefix token using binary search."""
        matches: set[int] = set()
        pos = bisect.bisect_left(self._sorted_name_tokens, tok)
        while pos < len(self._sorted_name_tokens) and self._sorted_name_tokens[pos].startswith(tok):
            matches.update(self._name_token_index[self._sorted_name_tokens[pos]])
            pos += 1
        return matches

    @lru_cache(maxsize=1024)
    def _search_indices(
        self,
        query: str,
        namespace: str | None,
        apiset: str,
        limit: int,
    ) -> tuple[int, ...]:
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

        # Fast-path: Exact Hash
        h_norm = q_lower.removeprefix("0x")
        if h_norm in self._by_hash:
            h_idx = self._by_hash[h_norm]
            if candidates is None or h_idx in candidates:
                return (h_idx,)

        # Fast-path: Exact Name
        exact_name_idx = self._by_name.get(q_lower)
        if exact_name_idx is not None and (candidates is None or exact_name_idx in candidates) and limit == 1:
            return (exact_name_idx,)

        query_tokens = _tokenize(q_raw)
        if not query_tokens:
            return ()

        token_matches: list[set[int]] = []
        for tok in query_tokens:
            tok_set = set(self._name_token_index.get(tok, set()))
            if len(tok) >= 3:
                tok_set.update(self._get_prefix_token_matches(tok))
            if tok in self._desc_token_index:
                tok_set.update(self._desc_token_index[tok])
            if candidates is not None:
                tok_set &= candidates
            token_matches.append(tok_set)

        token_count: dict[int, int] = defaultdict(int)
        for tok_set in token_matches:
            for c_idx in tok_set:
                token_count[c_idx] += 1

        if not token_count:
            return ()

        min_req = len(query_tokens) if len(query_tokens) <= 2 else max(2, int(len(query_tokens) * 0.6))
        valid = {c_idx: cnt for c_idx, cnt in token_count.items() if cnt >= min_req}
        if not valid and len(query_tokens) <= 3:
            max_cnt = max(token_count.values())
            valid = {c_idx: cnt for c_idx, cnt in token_count.items() if cnt == max_cnt}

        if not valid:
            return ()

        scored = []
        for c_idx, matched_count in valid.items():
            name_lower = self._all_records[c_idx]["name"].lower()
            score = matched_count * 100
            if name_lower == q_lower:
                score += 1000
            elif name_lower.startswith(q_lower):
                score += 500
            elif q_lower in name_lower:
                score += 300
            for tok in query_tokens:
                if tok in self._name_token_index and c_idx in self._name_token_index[tok]:
                    score += 50
            scored.append((score, c_idx))

        scored.sort(key=lambda x: x[0], reverse=True)
        return tuple(c_idx for _, c_idx in scored[:limit])

    def _format_summary(self, idx: int) -> dict[str, Any]:
        item = self._all_records[idx]
        params_str = ", ".join(
            f"{p.get('name', 'arg')}: {p.get('type', 'Any')}"
            for p in item.get("params", [])
        )
        desc = item.get("description", "")
        summary_line = desc.strip().split("\n")[0] if desc else ""
        if len(summary_line) > 120:
            summary_line = summary_line[:117] + "..."
        name_val = item["name"]
        return {
            "name": name_val,
            "hash": item["hash"],
            "namespace": item["ns"],
            "apiset": item["apiset"],
            "signature": f"{name_val}({params_str}) -> {item.get('results', 'void')}",
            "summary": summary_line,
        }

    def search(
        self,
        query: str,
        namespace: str | None = None,
        apiset: str = "all",
        limit: int = 10,
    ) -> list[dict[str, Any]]:
        """Search natives with ultra-fast inverted index and multi-word token scoring."""
        indices = self._search_indices(query, namespace, apiset, limit)
        return [self._format_summary(idx) for idx in indices]

    def get_detail(self, name_or_hash: str) -> dict[str, Any] | None:
        """Get full documentation and details for a native via O(1) dictionary lookup."""
        key = name_or_hash.strip().lower()
        idx = self._by_name.get(key)
        if idx is None:
            idx = self._by_hash.get(key.removeprefix("0x"))

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
