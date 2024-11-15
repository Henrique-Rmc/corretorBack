from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from app.db.db import get_db
from app.routes.auth import get_user, create_user, create_token, get_token
from app.schemas.usuario_schema import GetUser, PostUser, LoginUser
from app.utils import password

route = APIRouter(prefix="/auth", tags=["Authentication"])
oauth2bearer = OAuth2PasswordBearer(tokenUrl = 'auth/login')

@route.post("/cadastro", response_model=GetUser)
def register_user(payload: PostUser, db: Session = Depends(get_db)):
    if not payload.email:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Por Favor, insira o email",
        )
    user = get_user(db, payload.email)
    
    if user:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=f"Já existe um usuário com esse email",
        )
    hashed_password = password.secure_pwd(payload.hashed_password) 
    payload.hashed_password = hashed_password
    user = create_user(db, payload)
    print(user)
    return user