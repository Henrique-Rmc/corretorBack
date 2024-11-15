from pydantic import BaseModel, EmailStr
from typing import Optional, List, Dict
from datetime import datetime, date

class GetUser(BaseModel):
    email: EmailStr
    nome: Optional[str]
    
    class Config:
        title = "GetUsuario"
        orm_mode = True
        use_enum_values = True
        
class LoginUser(BaseModel):
    email: EmailStr
    senha: str
    
    class Config:
        title = "LoginUser Schema"
        orm_mode = True
        use_enum_values = True
        
class PostUser(BaseModel):
    nome: str
    email: EmailStr
    hashed_password: str
    
    class Config:
        orm_mode = True
        user_enum_values = True