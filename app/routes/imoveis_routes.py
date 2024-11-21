from fastapi import APIRouter, Depends, HTTPException, status
from app.db.db import get_db
from app.schemas.imovel_schema import GetImovel, ImovelCreate
from app.schemas.usuario_schema import GetUser, PostUser, LoginUser
from app.utils import password

route = APIRouter(prefix="/imoveis", tags=["Imoveis"])

# @route.post("/cadastro", response_model=dict)
# def imovel_create(
#     imovel: ImovelCreate,
#     db: Session = Depends(get_db),
#     corretor=Depends(get_current_corretor)
# )