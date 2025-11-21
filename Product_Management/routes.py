from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from .schemas import Product as ProductModel
from .model import ProductCreate, ProductRead
from .database import get_db

products_route = APIRouter(prefix="/products", tags=["Products"])


@products_route.get("/", response_model=list[ProductRead])
async def get_products(db: Session = Depends(get_db)):
    return db.query(ProductModel).all()


@products_route.get("/{product_id}", response_model=ProductRead)
async def get_product(product_id: int, db: Session = Depends(get_db)):
    product = db.query(ProductModel).filter(ProductModel.id == product_id).first()
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
    return product


@products_route.post("/", response_model=ProductRead, status_code=status.HTTP_201_CREATED)
async def add_product(product: ProductCreate, db: Session = Depends(get_db)):
    db_product = ProductModel(
        name=product.name,
        description=product.description,
        price=product.price,
        quantity=product.quantity,
    )
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


@products_route.put("/{product_id}", response_model=ProductRead)
async def update_product(product_id: int, updated: ProductCreate, db: Session = Depends(get_db)):
    product = db.query(ProductModel).filter(ProductModel.id == product_id).first()
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
    product.name = updated.name
    product.description = updated.description
    product.price = updated.price
    product.quantity = updated.quantity
    db.commit()
    db.refresh(product)
    return product


@products_route.delete("/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_product(product_id: int, db: Session = Depends(get_db)):
    product = db.query(ProductModel).filter(ProductModel.id == product_id).first()
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")
    db.delete(product)
    db.commit()
    return None