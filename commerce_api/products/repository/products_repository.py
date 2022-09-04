from typing import List, Union
from uuid import UUID

from fastapi import Depends

from commerce_api.db.models.products import Products
from commerce_api.products.dao.product_dao import ProductDAO
from commerce_api.products.exceptions.product_already_exists import \
    ProductAlreadyExistsError
from commerce_api.products.exceptions.product_not_exists import ProductNotExistsError
from commerce_api.products.repository.contracts import IRepository


class ProductsRepository(IRepository):
    model = Products

    def __init__(self, product_dao: ProductDAO = Depends()):
        self._product_dao = product_dao

    async def create(self, data) -> model:
        product = await self._product_dao.filter(name=data['name'])
        if product:
            raise ProductAlreadyExistsError()

        new_product = await self._product_dao.create(**data)
        return new_product

    async def update(self, product_id: Union[str, UUID], **fields) -> model:
        product = await self._product_dao.filter(id=product_id)
        if not product:
            raise ProductNotExistsError()

        updated_product = await self._product_dao.update(product, **fields)
        return updated_product

    async def filter(self, **fields) -> model:
        products = await self._product_dao.filter(**fields)
        return products

    async def get_paginated(self, offset: int = 0, limit: int = 10) -> List[model]:
        products = await self._product_dao.get_paginated(offset, limit)
        return products
