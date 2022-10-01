from abc import abstractmethod

from yarl import URL

from utils.enums.log_level import LogLevel


class ISettings:
    host: str
    port: int
    # quantity of workers for uvicorn
    workers_count: int
    # Enable uvicorn reloading
    reload: bool

    # Current environment
    environment_name: str

    log_level: LogLevel

    # Variables for the database
    db_host: str
    db_port: int
    db_user: str
    db_pass: str
    db_name: str
    db_echo: bool

    # Variables for the rabbitmq
    rabbit_host: str
    rabbit_port: int
    rabbit_user: str
    rabbit_pass: str
    rabbit_vhost: str
    rabbit_pool_size: int
    rabbit_channel_pool_size: int

    @property
    @abstractmethod
    def db_url(self) -> URL:
        """
        Assemble database URL from settings.

        :return: database URL.
        """
        raise NotImplementedError()

    @property
    @abstractmethod
    def rabbit_url(self) -> URL:
        """
        Assemble RabbitMQ URL from settings.

        :return: rabbit URL.
        """
        raise NotImplementedError()
