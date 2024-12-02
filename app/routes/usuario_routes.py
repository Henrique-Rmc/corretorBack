from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.controllers.usuario_controller import UsuarioController
from app.db.db import get_db
from app.models.usuario import Usuario
from app.schemas.usuario_schema import GetUser, PostUser, LoginUser
from app.utils.util_auth import create_access_token, create_refresh_token

usuario_route = APIRouter(prefix="/auth", tags=["Authentication"])
oauth2bearer = OAuth2PasswordBearer(tokenUrl = 'auth/login')

@usuario_route.post("/cadastro", response_model=GetUser)
def register_user(payload: PostUser, db: Session = Depends(get_db)):
    return UsuarioController.register_user(payload, db)


@usuario_route.post("/login", tags=["Authentication"])
def login_user(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    return UsuarioController.login_user(form_data, db)