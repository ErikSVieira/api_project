from pydantic import BaseModel, ConfigDict
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


class ProductsInputDTO(ProductBase):
    pass


class ProductsOutputDTO(ProductBase):
    id: UUID
    ative: bool
    created_at: datetime
    updated_at: datetime
    model_config = ConfigDict(from_attributes=True)
