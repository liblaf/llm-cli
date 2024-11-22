import pydantic_settings as ps

import llm_cli.utils as lu


class Config(ps.BaseSettings):
    model_config = ps.SettingsConfigDict(toml_file=[lu.get_app_dir() / "config.toml"])

    # https://docs.litellm.ai/docs/completion/input
    # Required Fields
    model: str = "deepseek/deepseek-chat"
    # Optional Fields
    temperature: float | None = None
    top_p: float | None = None

    @classmethod
    def settings_customise_sources(
        cls,
        settings_cls: type[ps.BaseSettings],
        init_settings: ps.PydanticBaseSettingsSource,
        env_settings: ps.PydanticBaseSettingsSource,
        dotenv_settings: ps.PydanticBaseSettingsSource,
        file_secret_settings: ps.PydanticBaseSettingsSource,
    ) -> tuple[ps.PydanticBaseSettingsSource, ...]:
        """Define the sources and their order for loading the settings values.

        Args:
            settings_cls: The Settings class.
            init_settings: The `InitSettingsSource` instance.
            env_settings: The `EnvSettingsSource` instance.
            dotenv_settings: The `DotEnvSettingsSource` instance.
            file_secret_settings: The `SecretsSettingsSource` instance.

        Returns:
            A tuple containing the sources and their order for loading the settings values.
        """
        return (
            init_settings,
            env_settings,
            dotenv_settings,
            file_secret_settings,
            ps.TomlConfigSettingsSource(settings_cls),
        )
