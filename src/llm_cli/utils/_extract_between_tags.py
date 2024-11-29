def extract_between_tags(content: str | None, tag: str = "Answer") -> str:
    if content is None:
        return ""
    content_lower: str = content.lower()
    opening_tag: str = f"<{tag}>".lower()
    start: int = content_lower.find(opening_tag)
    if start >= 0:
        start += len(opening_tag)
        content = content[start:]
    closing_tag: str = f"</{tag}>".lower()
    end: int = content_lower.find(closing_tag)
    if end >= 0:
        content = content[:end]
    return content.strip()