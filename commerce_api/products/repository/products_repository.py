from typing import List, Union
from uuid import UUID

from fastapi import Depends

from commerce_api.products.product_dao import ProductDAO
from commerce_api.products.entity import ProductsEntity
from commerce_api.products.events.sender.products_events_sender import ProductsEventsSender
from commerce_api.products.exceptions.product_already_exists import ProductAlreadyExistsError
from commerce_api.products.exceptions.product_not_exists import ProductNotExistsError
from commerce_api.products.repository.contracts import IProductsRepository
from commerce_api.products.types import ProductInputDict


class ProductsRepository(IProductsRepository):

    def __init__(self, product_dao: ProductDAO = Depends(), products_events_sender: ProductsEventsSender = Depends()):
        self._product_dao = product_dao
        self._products_events_sender = products_events_sender

    async def create_product(self, data: ProductInputDict) -> ProductsEntity:
        product = await self._product_dao.filter(name=data['name'])
        if product:
            raise ProductAlreadyExistsError()

        new_product = await self._product_dao.create(**data)
        await self._products_events_sender.sender(new_product.to_dict())
        return new_product

    async def update_product(self, product_id: Union[str, UUID], **fields) -> ProductsEntity:
        product = await self._product_dao.filter(id=product_id)
        if not product:
            raise ProductNotExistsError()

        updated_product = await self._product_dao.update(product, **fields)
        await self._products_events_sender.sender(updated_product.to_dict())
        return updated_product

    async def find_by_product_id(self, product_id: Union[str, UUID]) -> ProductsEntity:
        product = await self._product_dao.filter(id=product_id)
        if not product:
            raise ProductNotExistsError()
        return product

    async def get_paginated_products(self, offset: int = 0, limit: int = 10) -> List[ProductsEntity]:
        products = await self._product_dao.get_paginated(offset, limit)
        return products
