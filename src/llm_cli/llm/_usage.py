import litellm


def pretty_usage(response: litellm.ModelResponse) -> str:
    if "usage" not in response:
        return ""
    usage: litellm.Usage = response["usage"]
    cost: float = litellm.completion_cost(response)
    return f"""
Tokens : {usage.total_tokens} (Total) = {usage.prompt_tokens} (Prompt) + {usage.completion_tokens} (Completion)
Cost   : ${cost}
""".strip()
