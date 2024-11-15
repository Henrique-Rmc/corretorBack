#sqlalchemy é responsavel por transformar nossa classe python em um esquema
from sqlalchemy import Column, Integer, String

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Usuario(Base):
    __tablename__= "usuarios"
    
    id = Column(Integer, primary_key=True, index=True )
    nome = Column(String, nullable = False, index=True)
    email = Column(String, unique=True, index = True)
    hashed_password = Column(String, nullable=False)


class Token(Base):
    __tablename__ = "tokens"
    
    id = Column(Integer, primary_key=True, index=True)
    token = Column(String, index=True)
    user_id = Column(Integer)
    
    