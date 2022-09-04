from abc import ABC, abstractmethod
from typing import Union
from uuid import UUID

from commerce_api.db.base import Base


class IRepository(ABC):

    @property
    def model(self) -> Base:
        raise NotImplementedError()

    @abstractmethod
    async def update(self, product_id: Union[str, UUID], **fields) -> model:
        raise NotImplementedError()

    @abstractmethod
    async def create(self, **fields) -> model:
        raise NotImplementedError()

    @abstractmethod
    async def filter(self, **fields) -> model:
        raise NotImplementedError()

    @abstractmethod
    async def get_paginated(self, offset: int = 0, limit: int = 10) -> list:
        raise NotImplementedError()
