from abc import ABC, abstractmethod

from commerce_api.db.base import Base


class IRepository(ABC):

    @property
    def model(self) -> Base:
        raise NotImplementedError()

    @abstractmethod
    def update(self, **fields) -> model:
        raise NotImplementedError()

    @abstractmethod
    def create(self, **fields) -> model:
        raise NotImplementedError()

    @abstractmethod
    def filter(self, **fields) -> model:
        raise NotImplementedError()

    @abstractmethod
    def get_paginated(self) -> list:
        raise NotImplementedError()

    @abstractmethod
    def all(self) -> list:
        raise NotImplementedError()
