from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env')

    BASE_URL: str = 'https://visa.vfsglobal.com/blr/ru/pol/login'
    BOT_API: str
    DB_HOST: str
    DB_PORT: str
    DB_PASS: str
    DB_NAME: str
    DB_USER: str


    def get_db_link(self):
        return f''
    

config = Settings()