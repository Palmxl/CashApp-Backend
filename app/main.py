# CashApp/backend/app/main.py
import os
from app.routers import health, cards, transactions
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import Base, engine
from app.routers import health, cards  # cards
from app.routers import card_stats

# Cargar env
ENV_FILE = os.getenv("ENV_FILE", ".env.development")
load_dotenv(ENV_FILE)

# Crear tablas (por ahora tarjetas nada más)
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="CashApp API",
    version="0.1.0",
)

# CORS
origins = os.getenv("BACKEND_CORS_ORIGINS", "http://localhost:5173").split(",")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[o.strip() for o in origins],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Rutas
app.include_router(health.router)
app.include_router(cards.router, prefix="/cards", tags=["cards"])
app.include_router(transactions.router, prefix="/transactions", tags=["transactions"])
app.include_router(card_stats.router, prefix="/stats", tags=["stats"])

@app.get("/")
async def root():
    return {"message": "CashApp API running"}
