from typing import List, Optional
from sqlalchemy import ForeignKey, String, Text
from sqlalchemy.orm import relationship, mapped_column, Mapped
from app.models.base import Base

from app.models.foto_imovel import FotoImovel
from app.models.usuario import Usuario


class Imovel(Base):
    __tablename__="imoveis"
    
    id : Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String)
    cidade: Mapped[str]  = mapped_column(String)
    rua: Mapped[str] = mapped_column(String)
    tamanho: Mapped[str] = mapped_column(String)
    numero: Mapped[Optional[str]] = mapped_column(String)
    descricao: Mapped[Optional[str]] = mapped_column(String)
    valor: Mapped[str] = mapped_column(String)
    fotos: Mapped[List["FotoImovel"]] = relationship(
        "FotoImovel", back_populates="imovel", cascade="all, delete"
        )
    usuario_id : Mapped[str] = mapped_column(ForeignKey("usuarios.id"), nullable=False) 
    usuario: Mapped["Usuario"] = relationship("Usuario", back_populates="imoveis")