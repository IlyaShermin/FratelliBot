from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    bot_token: str
    admin_id: str
    payment_token: str
    gmail_app_password: str
    email_address: str
    email_password: str

    class Config:
        env_file = ".env"


settings = Settings()
