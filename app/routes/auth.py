from sqlalchemy.orm import Session
from app.models.usuario import *
from app.schemas.usuario_schema import PostUser
from pydantic import EmailStr

def get_user(db: Session, email: EmailStr):
    return db.query(Usuario).filter(Usuario.email == email).first()

def create_user(db: Session, usuario: PostUser):
    db_user = Usuario(nome=usuario.nome, email = usuario.email, hashed_password = usuario.hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_token(db: Session, token: str):
    return db.query(Token).filter(Token == token).first()

def create_token(db: Session, token: str, user_id: int):
    db_token = Token(token=token, user_id=user_id)
    db.add(db_token)
    db.commit()
    db.refresh(db_token)
    return db_token