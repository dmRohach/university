from fastapi import FastAPI

from .api import router


app = FastAPI()
app.include_router(router)


@app.get("/")
async def read_main():
    return {"msg": "Hello World"}
