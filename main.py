from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from app.routers import stocks, news, forex, portfolio
from app.db.db_config import SQLALCHEMY_DATABASE_URL
import asyncio


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(news.router)
app.include_router(stocks.router)
app.include_router(forex.router)
app.include_router(portfolio.router)

