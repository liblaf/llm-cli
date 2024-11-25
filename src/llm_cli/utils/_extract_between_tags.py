def extract_between_tags(content: str | None, tag: str = "Answer") -> str:
    if content is None:
        return ""
    start: int = content.find("<" + tag + ">")
    if start >= 0:
        start += len(tag) + 2
        content = content[start:]
    end: int = content.find("</" + tag + ">")
    if end >= 0:
        content = content[:end]
    return content.strip()
