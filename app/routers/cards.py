# CashApp/backend/app/routers/cards.py
from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app import models, schemas

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=List[schemas.Card])
def list_cards(db: Session = Depends(get_db)):
    return db.query(models.Card).all()

@router.post("/", response_model=schemas.Card, status_code=201)
def create_card(card: schemas.CardCreate, db: Session = Depends(get_db)):
    db_card = models.Card(**card.dict())
    db.add(db_card)
    db.commit()
    db.refresh(db_card)
    return db_card
