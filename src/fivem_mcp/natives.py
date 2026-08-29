import json
import os
from pathlib import Path
from typing import Any
import httpx

NATIVES_URL = "https://runtime.fivem.net/doc/natives.json"
DEFAULT_DATA_DIR = Path(__file__).resolve().parent.parent.parent / "data"
DEFAULT_DATA_FILE = DEFAULT_DATA_DIR / "natives.json"


class NativesManager:
    """Manages downloading, indexing, and searching FiveM native functions."""

    def __init__(self, data_file: Path | str | None = None):
        if data_file:
            self.data_file = Path(data_file)
        else:
            env_path = os.environ.get("FIVEM_NATIVES_PATH")
            self.data_file = Path(env_path) if env_path else DEFAULT_DATA_FILE

        self._loaded = False
        self._all_natives: list[dict[str, Any]] = []
        self._by_name: dict[str, dict[str, Any]] = {}
        self._by_hash: dict[str, dict[str, Any]] = {}
        self._namespaces: set[str] = set()

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
        """Load and index natives in memory."""
        if self._loaded and not force_reload:
            return

        self.ensure_data()
        with open(self.data_file, "r", encoding="utf-8") as f:
            raw_data: dict[str, dict[str, Any]] = json.load(f)

        self._all_natives.clear()
        self._by_name.clear()
        self._by_hash.clear()
        self._namespaces.clear()

        for namespace, natives_dict in raw_data.items():
            self._namespaces.add(namespace.upper())
            for hash_key, item in natives_dict.items():
                hash_val = item.get("hash") or hash_key
                name_val = item.get("name") or f"_{hash_val}"
                apiset_val = item.get("apiset", "client")

                record = {
                    **item,
                    "hash": hash_val,
                    "name": name_val,
                    "ns": namespace.upper(),
                    "apiset": apiset_val,
                }

                self._all_natives.append(record)
                self._by_hash[hash_val.lower()] = record
                self._by_name[name_val.lower()] = record

        self._loaded = True

    def search(
        self,
        query: str,
        namespace: str | None = None,
        apiset: str = "all",
        limit: int = 10,
    ) -> list[dict[str, Any]]:
        """Search natives by query string, namespace, and apiset."""
        self.load()
        q = query.strip().lower()
        ns_filter = namespace.strip().upper() if namespace else None
        apiset_filter = apiset.strip().lower() if apiset and apiset.lower() != "all" else None

        results = []
        for native in self._all_natives:
            if ns_filter and native["ns"] != ns_filter:
                continue

            native_apiset = native.get("apiset", "client").lower()
            if apiset_filter and apiset_filter != "all":
                if native_apiset != "shared" and native_apiset != apiset_filter:
                    continue

            name_lower = native["name"].lower()
            hash_lower = native["hash"].lower()
            desc = native.get("description", "")
            desc_lower = desc.lower()

            score = 0
            if q == name_lower or q == hash_lower:
                score = 100
            elif name_lower.startswith(q):
                score = 80
            elif q in name_lower:
                score = 60
            elif q in hash_lower:
                score = 40
            elif q in desc_lower:
                score = 20
            elif not q:
                score = 1

            if score > 0:
                params_str = ", ".join(
                    f"{p.get('name', 'arg')}: {p.get('type', 'Any')}"
                    for p in native.get("params", [])
                )
                summary_line = desc.strip().split("\n")[0] if desc else ""
                if len(summary_line) > 120:
                    summary_line = summary_line[:117] + "..."

                results.append((
                    score,
                    {
                        "name": native["name"],
                        "hash": native["hash"],
                        "namespace": native["ns"],
                        "apiset": native["apiset"],
                        "signature": f"{native['name']}({params_str}) -> {native.get('results', 'void')}",
                        "summary": summary_line,
                    }
                ))

        results.sort(key=lambda x: x[0], reverse=True)
        return [item[1] for item in results[:limit]]

    def get_detail(self, name_or_hash: str) -> dict[str, Any] | None:
        """Get full documentation and details for a native function."""
        self.load()
        key = name_or_hash.strip().lower()

        # Check by name first, then hash
        item = self._by_name.get(key) or self._by_hash.get(key)
        if not item and not key.startswith("0x"):
            item = self._by_hash.get(f"0x{key}")

        if not item:
            return None

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


# Global singleton instance
natives_manager = NativesManager()
