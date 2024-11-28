#sqlalchemy é responsavel por transformar nossa classe python em um esquema
from typing import List, Optional
from sqlalchemy import String, Text
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, mapped_column, Mapped
from app.models.base import Base
from app.models.imovel import Imovel


class Usuario(Base):
    __tablename__= "usuarios"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    nome : Mapped[str] = mapped_column(String)
    email : Mapped[str] = mapped_column(String)
    telefone : Mapped[Optional[str]] = mapped_column(String) 
    hashed_password: Mapped[str] = mapped_column(String)
    imoveis: Mapped[List[Imovel]] = relationship(
        "Imovel", back_populates="usuarios", cascade="all, delete"
    )
