from abc import ABC, abstractmethod

from commerce_api.db.base import Base


class IDAO(ABC):

    @property
    def model(self) -> Base:
        raise NotImplementedError()

    @abstractmethod
    async def update(self, _object: model, **fields) -> model:
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
