from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship
from app.db.database import Base

class Imovel(Base):
    __tablename__="imoveis"
    
    id = Column(Integer, primary_key = True, index=True)
    name = Column(String, nullable=False)
    city = Column(String, nullable = False)
    street = Column(String, nullable=False)
    size = Column(String, nullable=False)
    number = Column(String, nullable=False)
    description = Column(Text)
    
    fotos = relationship("FotoImovel", back_populates="imovel")