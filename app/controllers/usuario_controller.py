from fastapi import HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from app.schemas.usuario_schema import GetUser, PostUser
from sqlalchemy.orm import Session

from app.services.usuario_service import UsuarioService
from app.utils.util_auth import create_access_token, create_refresh_token

class UsuarioController:
    @staticmethod
    def register_user(payload: PostUser, db: Session) -> GetUser:
        try:
            user = UsuarioService.register_user(payload, db)
            return user
        except:
            raise HTTPException(
                status_code = 401,
                 detail="Credenciais Inválidas",
                 headers={"WWW-Authenticate": "Bearer"},
            )
            
                
    def login_user(form_data: OAuth2PasswordRequestForm, db: Session) -> dict:
        try:
            user= UsuarioService.login_authenticator(db, form_data)
            
        except:
            raise HTTPException(
                status_code = 401,
                 detail="Credenciais Inválidas",
                 headers={"WWW-Authenticate": "Bearer"},
            )
            
        access_token = create_access_token(subject=str(user.id))
        refresh_token = create_refresh_token(subject=str(user.id))
        return {
            "access_token": access_token,
            "refresh_token": refresh_token,
            "token_type": "bearer",
        }