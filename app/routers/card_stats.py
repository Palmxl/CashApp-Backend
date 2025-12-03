# CashApp/backend/app/routers/card_stats.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app import models

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/balance/{card_id}")
def get_card_balance(card_id: int, db: Session = Depends(get_db)):
    card = db.query(models.Card).filter(models.Card.id == card_id).first()

    if not card:
        raise HTTPException(status_code=404, detail="Card not found")

    txs = (
        db.query(models.Transaction)
        .filter(models.Transaction.card_id == card_id)
        .all()
    )

    purchases = sum(t.amount for t in txs if t.type in ["purchase", "installment"])
    payments = sum(t.amount for t in txs if t.type == "payment")

    balance = purchases - payments

    return {
        "card_id": card.id,
        "card_name": card.name,
        "credit_limit": card.credit_limit,
        "balance_used": balance,
        "available_credit": card.credit_limit - balance,
    }
