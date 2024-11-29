import functools

import litellm
import pydantic

import llm_cli.config as lcc


class ModelConfig(litellm.ModelConfig):
    tpm: int | None = None  # pyright: ignore [reportIncompatibleVariableOverride]
    rpm: int | None = None  # pyright: ignore [reportIncompatibleVariableOverride]


def default_model_list() -> list[ModelConfig]:
    lcc.init_litellm()
    QWEN_API_BASE: str = "https://dashscope.aliyuncs.com/compatible-mode/v1"  # noqa: N806
    QWEN_API_KEY: str | None = litellm.get_secret_str("QWEN_API_KEY")  # noqa: N806  # pyright: ignore [reportCallIssue]
    return [
        ModelConfig(
            model_name="deepseek-chat",
            litellm_params=litellm.CompletionRequest(model="deepseek/deepseek-chat"),
        ),
        ModelConfig(
            model_name="qwen-max",  # 32K
            litellm_params=litellm.CompletionRequest(
                model="openai/qwen-max",
                base_url=QWEN_API_BASE,
                api_key=QWEN_API_KEY,
            ),
        ),
        ModelConfig(
            model_name="qwen-plus",  # 128K
            litellm_params=litellm.CompletionRequest(
                model="openai/qwen-plus",
                base_url=QWEN_API_BASE,
                api_key=QWEN_API_KEY,
            ),
        ),
        ModelConfig(
            model_name="qwen-turbo",  # 1M
            litellm_params=litellm.CompletionRequest(
                model="openai/qwen-turbo",
                base_url=QWEN_API_BASE,
                api_key=QWEN_API_KEY,
            ),
        ),
        ModelConfig(
            model_name="qwen-long",  # 10M
            litellm_params=litellm.CompletionRequest(
                model="openai/qwen-long",
                base_url=QWEN_API_BASE,
                api_key=QWEN_API_KEY,
            ),
        ),
    ]


class RouterConfig(litellm.RouterConfig):
    model_list: list[ModelConfig] = pydantic.Field(default_factory=default_model_list)  # pyright: ignore [reportIncompatibleVariableOverride]
    num_retries: int = 3  # pyright: ignore [reportIncompatibleVariableOverride]
    fallbacks: list[dict[str, list[str]]] = pydantic.Field(  # pyright: ignore [reportIncompatibleVariableOverride]
        default_factory=lambda: [
            {"deepseek-chat": ["qwen-max", "qwen-plus", "qwen-turbo", "qwen-long"]}
        ]
    )

    @functools.cached_property
    def router(self) -> litellm.Router:
        return litellm.Router(
            **self.model_dump(
                exclude_unset=True, exclude_defaults=True, exclude_none=True
            )
        )
