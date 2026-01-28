from sqlalchemy import Column, Integer, Numeric, ForeignKey
from app.database import Base

class CompraDetalle(Base):
    __tablename__ = "compra_detalle"

    id = Column(Integer, primary_key=True, index=True)
    compra_id = Column(Integer, ForeignKey("compra.id"), nullable=False)
    producto_id = Column(Integer, ForeignKey("producto.id"), nullable=False)
    precio_u = Column(Numeric(10, 2), nullable=False)
    unidades = Column(Integer, nullable=False)
    subtotal = Column(Numeric(12, 2), nullable=False)
