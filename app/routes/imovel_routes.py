from fastapi import APIRouter, Depends, HTTPException, status
from app.controllers.imovel_controller import ImovelController
from app.db.db import get_db
from app.schemas.imovel_schema import GetImovel, ImovelCreate
from app.schemas.usuario_schema import GetUser, PostUser, LoginUser
from app.utils import password
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

imovel_route = APIRouter(prefix="/imoveis", tags=["Imoveis"])

@imovel_route.post("/cadastro", response_model=GetImovel)
def imovel_create(
    imovel: ImovelCreate,
    db: Session = Depends(get_db),
    token: str = Depends(oauth2_scheme)
    ):
    return ImovelController.create_imovel(imovel, db, token)   
    