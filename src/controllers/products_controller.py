from fastapi import HTTPException
from sqlalchemy.orm import Session
from src.models.product_model import Product
from src.schemas.product_schema import ProductsInputDTO
from uuid import UUID


def get_product(db: Session, id: UUID):
    product = db.query(Product).filter(Product.id == id).first()
    if product is None:
        raise HTTPException(
            status_code=404,
            detail=f"Produto com ID {id} não encontrado."
        )
    return product


def get_products(db: Session):
    return db.query(Product).all()


def create_product(db: Session, product: ProductsInputDTO):
    db_product = Product(**product.model_dump())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


def update_product(db: Session, id: UUID, product: ProductsInputDTO):
    db_product = get_product(db, id)
    if db_product:
        for key, value in product.model_dump().items():
            setattr(db_product, key, value)
        db.commit()
        db.refresh(db_product)
    return db_product


def delete_product(db: Session, id: UUID):
    db_product = get_product(db, id)
    if db_product:
        db.delete(db_product)
        db.commit()
    return {"message": f"Produto com ID {id} deletado com sucesso."}
