from typing import Union
from fastapi import FastAPI
from app.routes.usuario_routes import route

app = FastAPI()

app.include_router(route)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def red_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}