from pathlib import Path
from tempfile import gettempdir

from pydantic import BaseSettings, Field
from yarl import URL

from utils.enums.log_level import LogLevel

TEMP_DIR = Path(gettempdir())


class Settings(BaseSettings):
    """
    Application settings.

    These parameters can be configured
    with environment variables.
    """

    host: str = Field(default='127.0.0.1', env='SERVER_HOST')
    port: int = Field(default=8080, env='SERVER_PORT')  # noqa: WPS432
    # quantity of workers for uvicorn
    workers_count: int = Field(default=1, env='SERVER_WORKERS')
    # Enable uvicorn reloading
    reload: bool = Field(default=True, env='SERVER_RELOAD')

    # Current environment
    environment_name: str = Field(default='LOCAL', env='ENVIRONMENT_NAME')

    log_level: LogLevel = Field(default=LogLevel.INFO, env='LOG_LEVEL')

    # Variables for the database
    db_host: str = Field(default='localhost', env='DB_HOST')
    db_port: int = Field(default=5432, env='DB_PORT')  # noqa: WPS432
    db_user: str = Field(default='commerce_api', env='DB_USER')
    db_pass: str = Field(default='commerce_api', env='DB_PASS')
    db_name: str = Field(default='commerce_api', env='DB_NAME')
    db_echo: bool = Field(default=False, env='DB_ECHO')

    rabbit_host: str = Field(default='localhost', env='RABBIT_HOST')
    rabbit_port: int = Field(default=5672, env='RABBIT_PORT')
    rabbit_user: str = Field(default='guest', env='RABBIT_USER')
    rabbit_pass: str = Field(default='guest', env='RABBIT_PASS')
    rabbit_vhost: str = Field(default='/commerce_api', env='RABBIT_VHOST')
    rabbit_pool_size: int = Field(default=2, env='RABBIT_POOL_SIZE')
    rabbit_channel_pool_size: int = Field(default=10, env='RABBIT_CHANNEL_POOL_SIZE')

    @property
    def db_url(self) -> URL:
        """
        Assemble database URL from settings.

        :return: database URL.
        """
        return URL.build(
            scheme='postgresql+asyncpg',
            host=self.db_host,
            port=self.db_port,
            user=self.db_user,
            password=self.db_pass,
            path=f'/{self.db_name}',
        )

    @property
    def rabbit_url(self) -> URL:
        """
        Assemble RabbitMQ URL from settings.

        :return: rabbit URL.
        """
        return URL.build(
            scheme='amqp',
            host=self.rabbit_host,
            port=self.rabbit_port,
            user=self.rabbit_user,
            password=self.rabbit_pass,
            path=self.rabbit_vhost,
        )

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'


settings = Settings()
