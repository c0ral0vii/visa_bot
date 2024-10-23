from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env')

    BASE_URL: str = 'https://visa.vfsglobal.com/blr/ru/pol/login'