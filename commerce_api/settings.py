from pathlib import Path
from tempfile import gettempdir

from pydantic import BaseSettings, Field
from utils.enums.log_level import LogLevel
from yarl import URL

TEMP_DIR = Path(gettempdir())


class Settings(BaseSettings):
    """
    Application settings.

    These parameters can be configured
    with environment variables.
    """

    host: str = Field(default="127.0.0.1", env="SERVER_HOST")
    port: int = Field(default=8080, env="SERVER_PORT")  # noqa: WPS432
    # quantity of workers for uvicorn
    workers_count: int = Field(default=1, env="SERVER_WORKERS")
    # Enable uvicorn reloading
    reload: bool = Field(default=True, env="SERVER_RELOAD")

    # Current environment
    environment_name: str = Field(default="LOCAL", env="ENVIRONMENT_NAME")

    log_level: LogLevel = Field(default=LogLevel.INFO, env="LOG_LEVEL")

    # Variables for the database
    db_host: str = Field(default="localhost", env="DB_HOST")
    db_port: int = Field(default=5432, env="DB_PORT")  # noqa: WPS432
    db_user: str = Field(default="commerce_api", env="DB_USER")
    db_pass: str = Field(default="commerce_api", env="DB_PASS")
    db_name: str = Field(default="commerce_api", env="DB_NAME")
    db_echo: bool = Field(default=False, env="DB_ECHO")

    @property
    def db_url(self) -> URL:
        """
        Assemble database URL from settings.

        :return: database URL.
        """
        return URL.build(
            scheme="postgresql+asyncpg",
            host=self.db_host,
            port=self.db_port,
            user=self.db_user,
            password=self.db_pass,
            path=f"/{self.db_name}",
        )

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
