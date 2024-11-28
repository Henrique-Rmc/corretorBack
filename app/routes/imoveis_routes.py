from fastapi import APIRouter, Depends, HTTPException, status
from app.db.db import get_db
from app.schemas.imovel_schema import GetImovel, ImovelCreate
from app.schemas.usuario_schema import GetUser, PostUser, LoginUser
from app.utils import password
from sqlalchemy.orm import Session
from app.services.usuario_service import UserService

route = APIRouter(prefix="/imoveis", tags=["Imoveis"])

@route.post("/cadastro", response_model=dict)
def imovel_create(
    imovel: ImovelCreate,
    db: Session = Depends(get_db),
    corretor=Depends(UserService.get_current_user)
)