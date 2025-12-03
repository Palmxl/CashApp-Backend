# CashApp/backend/app/models.py

from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime

from app.database import Base


class Card(Base):
    __tablename__ = "cards"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    credit_limit = Column(Float, nullable=False)
    annual_rate = Column(Float, nullable=False)
    cutoff_day = Column(Integer, nullable=False)   # día de corte (1-31)
    payment_day = Column(Integer, nullable=False)  # día de pago (1-31)


class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    type = Column(String, nullable=False)  # purchase, payment, installment
    amount = Column(Float, nullable=False)
    description = Column(String, nullable=True)

    created_at = Column(DateTime, default=datetime.utcnow)

    card_id = Column(Integer, ForeignKey("cards.id"), nullable=False)
    card = relationship("Card")
