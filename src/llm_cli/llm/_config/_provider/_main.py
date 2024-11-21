import pydantic

from llm_cli import llm


class ProviderConfig(pydantic.BaseModel):
    deepseek: llm.DeepSeekConfig = llm.DeepSeekConfig()
