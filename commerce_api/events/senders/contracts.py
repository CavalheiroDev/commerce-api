from abc import abstractmethod

from aio_pika.exchange import Exchange


class EventsSender:
    exchange_name = None
    routing_key = None

    def __new__(cls, *args, **kwargs):
        if not cls.exchange_name and cls.routing_key:
            raise NotImplementedError('You must define exchange_name and routing_key')

        return super().__new__(cls)

    @abstractmethod
    async def sender(self, event) -> None:
        raise NotImplementedError()

    @abstractmethod
    async def get_exchange(self) -> Exchange:
        raise NotImplementedError()
