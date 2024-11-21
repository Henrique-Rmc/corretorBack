from fastapi import Depends
from sqlalchemy.orm import Session
from app.db.db import get_db
from app.db import db
from app.models.imovel import Imovel
from app.schemas.imovel_schema import ImovelCreate


class ImovelService:
    @staticmethod
    def cadastrar_imovel( db: Session ,imovel_data: ImovelCreate) -> Imovel:
        novo_imovel = Imovel(**imovel_data.model_dump())
        db.add(novo_imovel)
        db.commit()
        db.refresh(novo_imovel)
        return novo_imovel
    
