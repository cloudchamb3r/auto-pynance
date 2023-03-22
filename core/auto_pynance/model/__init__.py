"""
    handle postgres database
"""

from auto_pynance.model.base import BaseModel
from auto_pynance.model.ticker_data import TickerData
from dotenv import load_dotenv
from peewee import * 
import os


load_dotenv()
db = PostgresqlDatabase(
    database    = os.getenv("POSTGRES_DB"),
    host        = os.getenv("POSTGRES_HOST"),
    port        = os.getenv("POSTGRES_PORT"), 
    user        = os.getenv("POSTGRES_USER"),
    password    = os.getenv("POSTGRES_PASS")
)

db.create_tables([TickerData])

__all__ = ["BaseModel", "TickerData"]