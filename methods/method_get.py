from fastapi import FastAPI


class methodGet:
    app = FastAPI()

    @app.get("/")
    async def hello():
        return {"msg": "Welcome to FastAPI Framework"}
