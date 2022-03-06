from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def hello():
    return {"msg": "Welcome to FastAPI Framework"}
