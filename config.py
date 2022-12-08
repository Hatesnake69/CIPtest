from dotenv import load_dotenv
import os

load_dotenv()


class Settings:
    user: str = os.getenv("POSTGRES_USER")
    password: str = os.getenv("POSTGRES_PASSWORD")
    host: str = os.getenv("POSTGRES_HOST")
    port: str = os.getenv("POSTGRES_PORT")
    name: str = os.getenv("POSTGRES_NAME")
    timezone: str = os.getenv("TZ")


settings = Settings()
