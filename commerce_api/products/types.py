from typing import TypedDict


class ProductInputDict(TypedDict):
    name: str
    price: int
    stock_quantity: int
