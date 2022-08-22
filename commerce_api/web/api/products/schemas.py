from pydantic import BaseModel


class ProductInputDTO(BaseModel):
    name: str
    price: int
    stock_quantity: int
