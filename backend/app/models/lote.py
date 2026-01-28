from sqlalchemy import Column, Integer, Date, ForeignKey
from app.database import Base

class Lote(Base):
    __tablename__ = "lote"

    id = Column(Integer, primary_key=True, index=True)
    compra_detalle_id = Column(Integer, ForeignKey("compra_detalle.id"), nullable=False)
    producto_id = Column(Integer, ForeignKey("producto.id"), nullable=False)
    fecha_vencimiento = Column(Date)
    unidades = Column(Integer, nullable=False)
