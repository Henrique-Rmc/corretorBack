    
from app.models.usuario import Usuario
from app.schemas.usuario_schema import PostUser
from sqlalchemy.orm import Session

class UserRepo:
    
    def create_user(db: Session, usuario: PostUser):
        db_user = Usuario(nome=usuario.nome, email = usuario.email, hashed_password = usuario.hashed_password)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user

    def get_user_by_id(db: Session, user_id: str) -> Usuario:
        return db.query(Usuario).filter(Usuario.id == user_id).first()
        
    def get_user_by_email(db: Session, user_email: str) -> Usuario:
        return db.query(Usuario).filter(Usuario.email == user_email).first()
        