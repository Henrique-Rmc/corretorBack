from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base= declarative_base()

class FotoImovel(Base):
    __tablename__ = "fotos_imovel"
    
    id = Column(Integer, primary_key=True, index = True)
    imovel_id = Column(Integer, ForeignKey("imoveis.id"))
    foto_url = Column(String, nullable=True)
    
    imovel = relationship("Imovel", back_populates="fotos")