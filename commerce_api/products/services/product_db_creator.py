from fastapi import Depends

from commerce_api.products.entity import ProductsEntity
from commerce_api.products.enums import EventsTypeProductEnum
from commerce_api.products.events.sender.products_events_sender import ProductsEventsSender, EventsSender
from commerce_api.products.repository.products_repository import ProductsRepository, IProductsRepository
from commerce_api.products.types import ProductInputDict


class ProductDbCreator:
    def __init__(
        self,
        product_repository: IProductsRepository = Depends(ProductsRepository),
        product_events_sender: EventsSender = Depends(ProductsEventsSender),
    ):
        self._product_repository = product_repository
        self._product_events_sender = product_events_sender

    async def create_product(self, data: ProductInputDict) -> ProductsEntity:
        product = await self._product_repository.create_product(data=data)

        event = product.to_dict()
        event['event_type'] = EventsTypeProductEnum.CREATED.value

        await self._product_events_sender.send_event(event=event)

        return product
