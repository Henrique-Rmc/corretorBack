from fastapi import Depends, HTTPException
from app.models.usuario import Usuario
from app.schemas.imovel_schema import GetImovel, PostImovel
from sqlalchemy.orm import Session

from app.services.imovel_service import ImovelService
from app.services.usuario_service import UsuarioService

class ImovelController:
    
    def create_imovel(payload: PostImovel, db: Session, token: str) -> GetImovel:
        try:
            usuario = UsuarioService.get_current_user(token, db)
        except:
            raise HTTPException(
                    status_code = 401,
                    detail="Usuário Não Autenticado",
                    headers={"WWW-Authenticate": "Bearer"},
                )
        payload.id_usuario = usuario.id
        try:
            imovel = ImovelService.create_imovel(payload, db)
            return imovel
        except:
            raise HTTPException(
                status_code = 500,
                detail="Não Foi Possível Criar o Imóvel",
                headers={"WWW-Authenticate": "Bearer"},
            )