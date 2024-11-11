from sqlalchemy import Column, Integer, String, ForeignKey
from app.db.database import Base
from sqlalchemy.orm import relationship

class FotoImovel(Base):
    __tablename__ = "fotos_imovel"
    
    id = Column(Integer, primary_key=True, index = True)
    imovel_id = Column(Integer, ForeignKey("imoveis.id"))
    foto_url = Column(String, nullable=True)
    
    imovel = relationship("Imovel", back_populates="fotos")