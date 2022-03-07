from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel


class Book(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    price: float


chars_book = [
    {"min_pages": 20},
    {"max_pages": 1500},
    {"original": True}
]


app = FastAPI()


@app.get("/")
async def hello():
    return {"msg": "Welcome to FastAPI Framework"}


@app.post("/books/control/")
async def read_book(limit: Optional[int]):
    return chars_book


@app.post("/books/create/")
async def create_book(book: Book):
    return book


"""
See the documentation in:

1. http://127.0.0.1:8000/docs

2. http://127.0.0.1:8000/redoc
"""
