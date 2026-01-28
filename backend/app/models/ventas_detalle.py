from sqlalchemy import Column, Integer, Numeric, ForeignKey
from app.database import Base

class VentaDetalle(Base):
    __tablename__ = "ventas_detalle"

    id = Column(Integer, primary_key=True, index=True)
    venta_id = Column(Integer, ForeignKey("ventas.id"), nullable=False)
    lote_id = Column(Integer, ForeignKey("lote.id"), nullable=False)
    precio_u = Column(Numeric(10, 2), nullable=False)
    unidades = Column(Integer, nullable=False)
    subtotal = Column(Numeric(12, 2), nullable=False)
