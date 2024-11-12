from sqlalchemy import Column, Integer, String

from app.db.database import Base 

class Usuario(Base):
    __tablename__= "usuarios"
    
    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable = False)
    hashed_password = Column(String, nullable=False)
