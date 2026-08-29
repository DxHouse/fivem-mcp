import re
from collections import defaultdict
from pathlib import Path
from typing import Any

DOCS_DIR = Path(__file__).resolve().parent.parent.parent / "data" / "docs"
_TOKEN_RE = re.compile(r"[a-z0-9]+")
_HEADER_RE = re.compile(r"^#\s+(.+)$", re.MULTILINE)


def _tokenize(text: str) -> list[str]:
    return _TOKEN_RE.findall(text.lower()) if text else []


class DocsManager:
    """Manages loading, indexing, and searching FiveM Markdown developer guides."""

    def __init__(self, docs_dir: Path | None = None):
        self.docs_dir = Path(docs_dir) if docs_dir else DOCS_DIR
        self._docs: dict[str, dict[str, Any]] = {}
        self._title_tokens: dict[str, set[str]] = defaultdict(set)
        self._body_tokens: dict[str, set[str]] = defaultdict(set)
        self.load()

    def load(self) -> None:
        """Scan and index all Markdown files in docs_dir."""
        self._docs.clear()
        self._title_tokens.clear()
        self._body_tokens.clear()

        if not self.docs_dir.exists():
            return

        for path in self.docs_dir.glob("*.md"):
            slug = path.stem.lower()
            content = path.read_text(encoding="utf-8").lstrip("\ufeff")

            # Extract title from first # Header
            header_match = _HEADER_RE.search(content)
            title = header_match.group(1).strip() if header_match else slug.replace("-", " ").title()

            # Extract first non-header summary paragraph
            summary = ""
            for line in content.splitlines():
                line = line.strip()
                if line and not line.startswith("#") and not line.startswith("```") and not line.startswith("-"):
                    summary = line
                    break
            if len(summary) > 140:
                summary = summary[:137] + "..."

            self._docs[slug] = {
                "slug": slug,
                "title": title,
                "summary": summary,
                "content": content,
            }

            for tok in _tokenize(title):
                self._title_tokens[tok].add(slug)
            for tok in _tokenize(content):
                self._body_tokens[tok].add(slug)

    def search(self, query: str, limit: int = 5) -> list[dict[str, Any]]:
        """Search documentation topics by query string."""
        q_raw = query.strip()
        if not q_raw:
            return self.list_topics()[:limit]

        q_slug = q_raw.lower().replace("_", "-")
        if q_slug in self._docs:
            doc = self._docs[q_slug]
            return [{
                "topic": doc["slug"],
                "title": doc["title"],
                "summary": doc["summary"],
            }]

        tokens = _tokenize(q_raw)
        if not tokens:
            return []

        # Count token matches per slug
        scores: dict[str, int] = defaultdict(int)
        for tok in tokens:
            for slug in self._title_tokens.get(tok, set()):
                scores[slug] += 50
            for slug in self._body_tokens.get(tok, set()):
                scores[slug] += 10

        if not scores:
            return []

        ranked = sorted(scores.items(), key=lambda x: x[1], reverse=True)
        results = []
        for slug, _ in ranked[:limit]:
            doc = self._docs[slug]
            results.append({
                "topic": doc["slug"],
                "title": doc["title"],
                "summary": doc["summary"],
            })
        return results

    def get_doc(self, topic: str) -> str | None:
        """Get full markdown content by topic slug or title."""
        slug = topic.strip().lower().replace("_", "-")
        doc = self._docs.get(slug)
        if doc:
            return doc["content"]

        for s, d in self._docs.items():
            if slug in s or s in slug or slug in d["title"].lower():
                return d["content"]
        return None

    def list_topics(self) -> list[dict[str, Any]]:
        """List all available documentation topics."""
        return [
            {
                "topic": d["slug"],
                "title": d["title"],
                "summary": d["summary"],
            }
            for d in self._docs.values()
        ]


# Global singleton instance
docs_manager = DocsManager()
