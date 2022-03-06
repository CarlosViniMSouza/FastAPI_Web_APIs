from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel


class Book(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    price: float


app = FastAPI()


@app.get("/")
async def hello():
    return {"msg": "Welcome to FastAPI Framework"}


@app.post("/books/")
async def create_book(book: Book):
    return book


"""
See the documentation in:

1. http://127.0.0.1:8000/docs

2. http://127.0.0.1:8000/redoc
"""
