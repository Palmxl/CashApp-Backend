# CashApp/backend/app/schemas.py
from pydantic import BaseModel, Field
from typing import List

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
