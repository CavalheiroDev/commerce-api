from abc import abstractmethod

from utils.entity import Entity


class ProductsEntity(Entity):
    name: str
    price: int
    stock_quantity: int

    @abstractmethod
    def to_dict(self) -> dict:
        raise NotImplementedError()
