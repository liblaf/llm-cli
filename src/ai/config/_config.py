import litellm
import pydantic_settings as ps

import ai.config as aic
import ai.utils as aiu


class Config(ps.BaseSettings):
    model_config = ps.SettingsConfigDict(toml_file=[aiu.get_app_dir() / "config.toml"])

    completion: litellm.CompletionRequest = litellm.CompletionRequest(
        model="deepseek-chat"
    )
    router: aic.RouterConfig = aic.RouterConfig()

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
