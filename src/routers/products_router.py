from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session
from uuid import UUID

from src.schemas.product_schema import ProductsInputDTO, ProductsOutputDTO
from src.controllers import products_controller as pc
from src.core.database import get_db

router = APIRouter(prefix="/products", tags=["Products"])


@router.get(
    "/",
    response_model=list[ProductsOutputDTO],
    status_code=status.HTTP_200_OK,
)
def get_products(db: Session = Depends(get_db)):
    return pc.get_products(db)


@router.get(
    "/{id}",
    response_model=ProductsOutputDTO,
    status_code=status.HTTP_200_OK,
)
def get_product(id: UUID, db: Session = Depends(get_db)):
    return pc.get_product(db, id)


@router.post(
    "/",
    response_model=ProductsOutputDTO,
    status_code=status.HTTP_201_CREATED,
)
def create_product(
    product: ProductsInputDTO,
    db: Session = Depends(get_db),
):
    return pc.create_product(db, product)


@router.put(
    "/{id}",
    response_model=ProductsOutputDTO,
    status_code=status.HTTP_200_OK,
)
def update_product(
    id: UUID,
    product: ProductsInputDTO,
    db: Session = Depends(get_db),
):
    return pc.update_product(db, id, product)


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_product(id: UUID, db: Session = Depends(get_db)):
    return pc.delete_product(db, id)
