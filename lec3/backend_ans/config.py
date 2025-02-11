from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    uri: str
    dc_name: str
    secret_key: str
    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()

URI = settings.uri
DC_NAME = settings.dc_name
SECRET_KEY = settings.secret_key

