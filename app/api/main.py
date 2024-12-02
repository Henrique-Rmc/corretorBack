from typing import Union
from fastapi import FastAPI
from app.routes.usuario_routes import usuario_route
from app.routes.imovel_routes import imovel_route

app = FastAPI()

app.include_router(usuario_route)
app.include_router(imovel_route)


@app.get("/")
def read_root():
    return {"Hello": "World"}


