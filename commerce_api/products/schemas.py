from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


class ProductInputDTO(BaseModel):
    name: str
    price: int
    stock_quantity: int

    class Config:
        orm_mode = True


class ProductOutputDTO(BaseModel):
    id: UUID
    name: str
    stock_quantity: int
    price: int
    created: datetime
    modified: datetime

    class Config:
        orm_mode = True


class ProductAlreadyExists(BaseModel):
    message: str
    code: str


class ProductNotExists(BaseModel):
    message: str
    code: str
