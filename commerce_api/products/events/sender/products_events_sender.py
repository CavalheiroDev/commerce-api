from aio_pika import Channel, Exchange, Message
from aio_pika.pool import Pool
from fastapi import Depends

from commerce_api.events.dependencies import get_rmq_channel_pool
from commerce_api.events.senders.contracts import EventsSender
import ujson


class ProductsEventsSender(EventsSender):
    exchange_name = 'e.products'
    routing_key = 'products'

    def __init__(self, channel_pool: Pool[Channel] = Depends(get_rmq_channel_pool)):
        self._channel_pool = channel_pool

    async def sender(self, event: dict) -> None:
        exchange = await self.get_exchange()
        message = Message(
            body=ujson.dumps(event).encode('utf-8'),
            content_type='application/json',
        )
        await exchange.publish(message=message, routing_key=self.routing_key)

    async def get_exchange(self) -> Exchange:
        async with self._channel_pool.acquire() as connection:
            exchange = await connection.get_exchange(name=self.exchange_name)
            return exchange
