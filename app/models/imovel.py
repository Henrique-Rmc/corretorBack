from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship
from app.db.database import Base

class Imovel(Base):
    __tablename__="imoveis"
    
    id = Column(Integer, primary_key = True, index=True)
    nome = Column(String, nullable=False)
    cidade = Column(String, nullable = False)
    rua = Column(String, nullable=False)
    tamanho = Column(String, nullable=False)
    numero = Column(String)
    descricao = Column(Text)
    
    fotos = relationship("FotoImovel", back_populates="imovel")