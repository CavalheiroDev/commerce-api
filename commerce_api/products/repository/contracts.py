from abc import ABC, abstractmethod
from typing import Union, List
from uuid import UUID

from commerce_api.products.entity import ProductsEntity
from commerce_api.products.types import ProductInputDict


class IProductsRepository(ABC):

    @abstractmethod
    async def update_product(self, product_id: Union[str, UUID], **fields) -> ProductsEntity:
        raise NotImplementedError()

    @abstractmethod
    async def create_product(self, data: ProductInputDict) -> ProductsEntity:
        raise NotImplementedError()

    @abstractmethod
    async def get_paginated_products(self, offset: int = 0, limit: int = 10) -> List[ProductsEntity]:
        raise NotImplementedError()

    @abstractmethod
    async def find_by_product_id(self, product_id: Union[str, UUID]) -> ProductsEntity:
        raise NotImplementedError()
