import litellm
from rich.panel import Panel


def pretty_usage(response: litellm.ModelResponse) -> str:
    if "usage" not in response:
        return ""
    usage: litellm.Usage = response["usage"]
    cost: float = litellm.completion_cost(response)
    return f"""
Tokens : {usage.total_tokens} (Total) = {usage.prompt_tokens} (Prompt) + {usage.completion_tokens} (Completion)
Cost   : ${cost}
""".strip()


def usage_panel(response: litellm.ModelResponse, *, expand: bool = False) -> Panel:
    return Panel(pretty_usage(response), expand=expand)
