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

class PostImovel(ImovelBase):
    pass
    
class GetImovel(ImovelBase):
    pass
    
class ImovelCreate(ImovelBase):
    fotos : Optional[List[FotoImovelCreate]] = []
    
class Imovel(ImovelBase):
    fotos: List[FotoImovel] = []
    
    class Config:
        from_attributes = True