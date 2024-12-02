from pydantic import EmailStr
from fastapi import Depends, HTTPException, Request
from app.config import setting
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import jwt
from passlib.context import CryptContext

from app.db.db import get_db
from app.schemas.usuario_schema import PostUser
from app.utils.password import secure_pwd
from app.utils.util_auth import verify_password
from app.models import *
from app.schemas import *
from app.repositories.user_repo import  UserRepo


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")


class UsuarioService:
    def get_current_user(
        token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)) -> Usuario:
        try:
            payload = jwt.decode(token, setting.secret_key, algorithms=[setting.algorithm])
            user_id: str = payload.get("sub")
            if user_id is None:
                raise HTTPException(
                    status_code=401, detail="Token invalido ou expirado"
                )
            user = UserRepo.get_user_by_id(db, user_id)
            if user is None:
                raise HTTPException(
                    status_code=401, detail="Usuário não encontrado"
                )
            return user
        except jwt.ExpiredSignatureError:
            raise HTTPException(status_code=401, detail="Token Expirado")
        except jwt.InvalidTokenError:
            raise HTTPException(status_code=401, detail="Token Inválido")

    @staticmethod
    def register_user(payload: PostUser, db: Session) -> Usuario:
        """
        Lógica para cadastro de usuário.
        """
        if not payload.email:
            raise HTTPException(
                status_code=401,
                detail="Por Favor, insira o email",
            )

        user = UserRepo.get_user_by_email(db, payload.email)

        if user:
            raise HTTPException(
                status_code=401,
                detail=f"Já existe um usuário com esse email",
            )

        hashed_password = secure_pwd(payload.hashed_password)
        payload.hashed_password = hashed_password

        return UserRepo.create_user(db, payload)
    

            
    def login_authenticator(db: Session, form_data: OAuth2PasswordRequestForm):
        try:
            user = UserRepo.get_user_by_email(db, form_data.username)
            if not user:
                raise HTTPException(
                    status_code=401, detail="Usuário não existente"
                )
            if not verify_password(form_data.password, user.hashed_password):
                raise HTTPException(
                    status_code=401, detail="Senha Inválida"
                )
            return user
        except jwt.InvalidSignatureError:
            raise HTTPException(status_code=401, detail="Não Foi possível realizar o Login")
        
    

             