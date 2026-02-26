from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, engine
import models

# Create tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Product Service")

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# -------------------
# CREATE PRODUCT
# -------------------
@app.post("/products")
def create_product(name: str, price: float, user_id: int, db: Session = Depends(get_db)):
    product = models.Product(name=name, price=price, user_id=user_id)
    db.add(product)
    db.commit()
    db.refresh(product)
    return product

# -------------------
# GET ALL PRODUCTS
# -------------------
@app.get("/products")
def get_products(db: Session = Depends(get_db)):
    return db.query(models.Product).all()

# -------------------
# GET PRODUCT BY ID
# -------------------
@app.get("/products/{product_id}")
def get_product(product_id: int, db: Session = Depends(get_db)):
    product = db.query(models.Product).filter(models.Product.id == product_id).first()

    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    return product

# -------------------
# DELETE PRODUCT
# -------------------
@app.delete("/products/{product_id}")
def delete_product(product_id: int, db: Session = Depends(get_db)):
    product = db.query(models.Product).filter(models.Product.id == product_id).first()

    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    db.delete(product)
    db.commit()

    return {"message": "Product deleted successfully"}