from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.database import SessionLocal
from app import models, schemas

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=List[schemas.Transaction])
def list_transactions(db: Session = Depends(get_db)):
    return db.query(models.Transaction).order_by(models.Transaction.created_at.desc()).all()

@router.post("/", response_model=schemas.Transaction, status_code=201)
def create_transaction(tx: schemas.TransactionCreate, db: Session = Depends(get_db)):
    # validar tipo
    valid_types = ["purchase", "payment", "installment"]
    if tx.type not in valid_types:
        raise HTTPException(status_code=400, detail="Invalid transaction type")

    # validar tarjeta
    card = db.query(models.Card).filter(models.Card.id == tx.card_id).first()
    if not card:
        raise HTTPException(status_code=404, detail="Card not found")

    # crear transacción
    new_tx = models.Transaction(**tx.dict())
    db.add(new_tx)
    db.commit()
    db.refresh(new_tx)

    return new_tx
