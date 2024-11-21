import openai
import pydantic


class BaseProviderConfig(pydantic.BaseModel):
    api_key: str | None = None
    base_url: str | None = None

    @property
    def client(self) -> openai.OpenAI:
        return openai.OpenAI(api_key=self.api_key, base_url=self.base_url)

    @property
    def async_client(self) -> openai.AsyncOpenAI:
        return openai.AsyncOpenAI(api_key=self.api_key, base_url=self.base_url)
