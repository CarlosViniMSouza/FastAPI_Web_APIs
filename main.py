from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def hello():
    return {"msg": "Welcome to FastAPI Framework"}


@app.get("/book/id_book")
async def checking_book(id_book: int):
    return {"msg": f"The book founding is {id_book}"}

"""
See the documentation in:

1. http://127.0.0.1:8000/docs

2. http://127.0.0.1:8000/redoc
"""
