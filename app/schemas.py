# CashApp/backend/app/schemas.py
from pydantic import BaseModel, Field
from typing import List
from datetime import datetime

class CardBase(BaseModel):
    name: str
    credit_limit: float = Field(gt=0)
    annual_rate: float = Field(gt=0)
    cutoff_day: int = Field(ge=1, le=31)
    payment_day: int = Field(ge=1, le=31)

class CardCreate(CardBase):
    pass

class Card(CardBase):
    id: int

    class Config:
        orm_mode = True

# Por si luego quieres listar
CardList = list[Card]

class TransactionBase(BaseModel):
    type: str  # purchase, payment, installment
    amount: float
    description: str | None = None
    card_id: int

class TransactionCreate(TransactionBase):
    pass

class Transaction(TransactionBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
