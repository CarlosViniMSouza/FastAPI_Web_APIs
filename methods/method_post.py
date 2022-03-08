from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

chars_book = [
    {"min_pages": 20},
    {"max_pages": 1500},
    {"original": True}
]


class Book(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    price: float


class methodPost:
    app = FastAPI()

    @app.post("/books/control/")
    async def read_book():
        return chars_book

    @app.post("/books/create/")
    async def create_book(book: Book):
        return book
