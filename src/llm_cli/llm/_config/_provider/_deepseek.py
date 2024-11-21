from llm_cli import llm


class DeepSeekConfig(llm.BaseProviderConfig):
    api_key: str | None = None
    base_url: str | None = "https://api.deepseek.com"
