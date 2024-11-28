from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.db.db import get_db
from app.models.usuario import Usuario
from app.schemas.usuario_schema import GetUser, PostUser, LoginUser
from app.services.usuario_service import UserService
from app.utils import password
from app.utils.util_auth import create_access_token, create_refresh_token

route = APIRouter(prefix="/auth", tags=["Authentication"])
oauth2bearer = OAuth2PasswordBearer(tokenUrl = 'auth/login')

@route.post("/cadastro", response_model=GetUser)
def register_user(payload: PostUser, db: Session = Depends(get_db)):
    try:
        user = UserService.register_user(payload, db)
        return user
    except HTTPException as e:
        raise e

@route.post("/loginCorretor", tags=["Authentication"])
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = UserService.login_authenticator(db, form_data)
    if not user:
        raise HTTPException(
        status_code=401,
        detail="Credenciais inválidas",
        headers={"WWW-Authenticate": "Bearer"},
    )
    access_token = create_access_token(subject=str(user.id))
    refresh_token = create_refresh_token(subject=str(user.id))
    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer"
    }