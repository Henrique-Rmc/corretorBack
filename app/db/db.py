from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from app.config import setting

# Construção da URL de conexão com o banco de dados
database_url = f"postgresql://{setting.db_usr}:{setting.db_pwd}@{setting.db_host}:{setting.db_port}/{setting.db_name}"

# Cria o engine do SQLAlchemy
engine = create_engine(database_url)

# Configura o sessionmaker com o engine criado
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para as classes de modelo
Base = declarative_base()

# Dependência do banco de dados
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
