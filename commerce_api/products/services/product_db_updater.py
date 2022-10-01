from typing import Union
from uuid import UUID

from fastapi import Depends

from commerce_api.products.entity import ProductsEntity
from commerce_api.products.enums import EventsTypeProductEnum
from commerce_api.products.events.sender.products_events_sender import ProductsEventsSender, EventsSender
from commerce_api.products.repository.products_repository import ProductsRepository, IProductsRepository
from commerce_api.products.types import ProductInputDict


class ProductDbUpdater:
    def __init__(
        self,
        product_repository: IProductsRepository = Depends(ProductsRepository),
        product_events_sender: EventsSender = Depends(ProductsEventsSender),
    ):
        self._product_repository = product_repository
        self._product_events_sender = product_events_sender

    async def update_product(self, product_id: Union[str, UUID], data: ProductInputDict) -> ProductsEntity:
        product = await self._product_repository.update_product(product_id=product_id, **data)

        event = product.to_dict()
        event['event_type'] = EventsTypeProductEnum.UPDATED.value

        await self._product_events_sender.send_event(event=event)

        return product
