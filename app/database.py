# CashApp/backend/app/database.py
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

ENV_FILE = os.getenv("ENV_FILE", ".env.development")
load_dotenv(ENV_FILE)

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./cashapp.db")

connect_args = {}
if DATABASE_URL.startswith("sqlite"):
    connect_args = {"check_same_thread": False}

engine = create_engine(DATABASE_URL, connect_args=connect_args)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
