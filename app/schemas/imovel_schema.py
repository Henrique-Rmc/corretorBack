from pydantic import BaseModel
from typing import List, Optional

class FotoImovelBase(BaseModel):
    foto_url: str
    
class FotoImovelCreate(FotoImovelBase):
    pass

class FotoImovel(FotoImovelBase):
    id: int
    
    class Config:
        from_attributes = True
        
class ImovelBase(BaseModel):
    nome: str
    cidade: str
    rua: str
    tamanho : str
    numero : str
    descricao : Optional[str] = None
    
class ImovelCreate(ImovelBase):
    fotos : List[FotoImovelCreate] = []
    
class Imovel(ImovelBase):
    id: int
    fotos: List[FotoImovel] = []
    
    class Config:
        from_attributes = True