from pydantic import BaseModel
from uuid import UUID

from datetime import datetime


class ProductBase(BaseModel):
    name: str
    type: str
    size: int
    mark: str
    model: str
    qty: int
    buy_price: float
    sale_price: float

    class Config:
        from_attributes = True


class ProductsInputDTO(ProductBase):
    pass


class ProductsOutputDTO(ProductBase):
    id: UUID
    ative: bool
    created_at: datetime
    updated_at: datetime
