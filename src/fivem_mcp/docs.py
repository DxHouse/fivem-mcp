import re
from collections import defaultdict
from pathlib import Path
from typing import Any

_PKG_DOCS_DIR = Path(__file__).resolve().parent / "data" / "docs"
_REPO_DOCS_DIR = Path(__file__).resolve().parent.parent.parent / "data" / "docs"
DOCS_DIR = _PKG_DOCS_DIR if _PKG_DOCS_DIR.exists() else _REPO_DOCS_DIR
_TOKEN_RE = re.compile(r"[a-z0-9]+")
_FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)
_HEADER_RE = re.compile(r"^#\s+(.+)$", re.MULTILINE)


def _tokenize(text: str) -> list[str]:
    return _TOKEN_RE.findall(text.lower()) if text else []


def _parse_frontmatter(raw_text: str) -> tuple[dict[str, Any], str]:
    """Extract YAML frontmatter key-values and remaining markdown body without external YAML dependency."""
    fm: dict[str, Any] = {}
    body = raw_text

    match = _FRONTMATTER_RE.match(raw_text)
    if match:
        fm_block = match.group(1)
        body = raw_text[match.end():]
        for line in fm_block.splitlines():
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            if ":" in line:
                key, val = line.split(":", 1)
                key = key.strip().lower()
                val = val.strip().strip("\"'")
                if val.startswith("[") and val.endswith("]"):
                    # Parse list of strings: [a, b, c]
                    items = [item.strip().strip("\"'") for item in val[1:-1].split(",") if item.strip()]
                    fm[key] = items
                else:
                    fm[key] = val
    return fm, body


class DocsManager:
    """Manages loading, frontmatter indexing, and high-precision searching of FiveM Markdown developer guides."""

    def __init__(self, docs_dir: Path | None = None):
        self.docs_dir = Path(docs_dir) if docs_dir else DOCS_DIR
        self._docs: dict[str, dict[str, Any]] = {}
        self._keyword_tokens: dict[str, set[str]] = defaultdict(set)
        self._title_tokens: dict[str, set[str]] = defaultdict(set)
        self._body_tokens: dict[str, set[str]] = defaultdict(set)
        self.load()

    def load(self) -> None:
        """Scan and index all Markdown files in docs_dir."""
        self._docs.clear()
        self._keyword_tokens.clear()
        self._title_tokens.clear()
        self._body_tokens.clear()

        if not self.docs_dir.exists():
            return

        for path in self.docs_dir.glob("*.md"):
            # Skip readme or index catalog from topic slugs
            if path.name.lower() in ("readme.md", "index.md"):
                continue

            slug = path.stem.lower()
            raw_content = path.read_text(encoding="utf-8").lstrip("\ufeff")
            fm, body = _parse_frontmatter(raw_content)

            # Title extraction: Frontmatter title -> First # Header -> Formatted Slug
            title = fm.get("title")
            if not title:
                header_match = _HEADER_RE.search(body)
                title = header_match.group(1).strip() if header_match else slug.replace("-", " ").title()

            # Summary extraction: Frontmatter description -> First non-header paragraph
            summary = fm.get("description")
            if not summary:
                for line in body.splitlines():
                    line = line.strip()
                    if line and not line.startswith("#") and not line.startswith("```") and not line.startswith("-") and not line.startswith(">"):
                        summary = line
                        break
            if summary and len(summary) > 140:
                summary = summary[:137] + "..."

            keywords = fm.get("keywords", [])
            if isinstance(keywords, str):
                keywords = [k.strip() for k in keywords.split(",") if k.strip()]

            self._docs[slug] = {
                "slug": slug,
                "title": title,
                "summary": summary or "",
                "keywords": keywords,
                "content": raw_content,
                "body": body,
            }

            # Indexing with token priority
            for kw in keywords:
                for tok in _tokenize(kw):
                    self._keyword_tokens[tok].add(slug)

            for tok in _tokenize(title):
                self._title_tokens[tok].add(slug)

            for tok in _tokenize(body):
                self._body_tokens[tok].add(slug)

    def search(self, query: str, limit: int = 5) -> list[dict[str, Any]]:
        """Search documentation topics with keyword synonym weighting and multi-token scoring."""
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

        scores: dict[str, int] = defaultdict(int)
        for tok in tokens:
            # Keyword synonyms receive top priority (+100)
            for slug in self._keyword_tokens.get(tok, set()):
                scores[slug] += 100
            # Title matches (+50)
            for slug in self._title_tokens.get(tok, set()):
                scores[slug] += 50
            # Body matches (+10)
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
