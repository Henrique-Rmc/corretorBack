from sqlalchemy import ForeignKey, String

from app.models.base import Base
from sqlalchemy.orm import relationship, mapped_column, Mapped

class FotoImovel(Base):
    __tablename__ = "fotos_imoveis"
    
    id : Mapped[int] = mapped_column(primary_key=True)
    imovel_id : Mapped[int] = mapped_column(ForeignKey("imoveis.id", ondelete="CASCADE"))
    foto_url: Mapped[str] = mapped_column(String)
    
    imovel = relationship("Imovel", back_populates="fotos")