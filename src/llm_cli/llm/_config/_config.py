from pathlib import Path
from typing import Literal

import openai
import pydantic_settings as ps
import typer

from llm_cli import llm


class Config(ps.BaseSettings):
    model_config = ps.SettingsConfigDict(
        toml_file=[Path(typer.get_app_dir("llm-cli")) / "models.toml"]
    )
    model: str = "deepseek-chat"
    provider: Literal["deepseek", "custom"] = "deepseek"
    providers: llm.ProviderConfig = llm.ProviderConfig()

    @classmethod
    def settings_customise_sources(
        cls,
        settings_cls: type[ps.BaseSettings],
        init_settings: ps.PydanticBaseSettingsSource,
        env_settings: ps.PydanticBaseSettingsSource,
        dotenv_settings: ps.PydanticBaseSettingsSource,
        file_secret_settings: ps.PydanticBaseSettingsSource,
    ) -> tuple[ps.PydanticBaseSettingsSource, ...]:
        return (
            init_settings,
            env_settings,
            dotenv_settings,
            file_secret_settings,
            ps.TomlConfigSettingsSource(settings_cls),
        )

    @property
    def provider_config(self) -> llm.BaseProviderConfig:
        return getattr(self.providers, self.provider)

    @property
    def client(self) -> openai.OpenAI:
        return self.provider_config.client

    @property
    def async_client(self) -> openai.AsyncOpenAI:
        return self.provider_config.async_client
