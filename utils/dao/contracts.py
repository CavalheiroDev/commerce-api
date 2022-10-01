from abc import ABC, abstractmethod
from typing import Type, List

from utils.entity import Entity


class IDAO(ABC):
    model: Type[Entity]

    @abstractmethod
    async def update(self, entity: Entity, **fields) -> Entity:
        raise NotImplementedError()

    @abstractmethod
    async def create(self, **fields) -> Entity:
        raise NotImplementedError()

    @abstractmethod
    async def filter(self, **fields) -> Entity:
        raise NotImplementedError()

    @abstractmethod
    async def get_paginated(self, offset: int = 0, limit: int = 10) -> List[Entity]:
        raise NotImplementedError()
