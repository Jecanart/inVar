from sqlalchemy import Column, Integer, Date, String, ForeignKey
from app.database import Base

class Movimiento(Base):
    __tablename__ = "movimientos"

    id = Column(Integer, primary_key=True, index=True)
    lote_id = Column(Integer, ForeignKey("lote.id"), nullable=False)
    fecha = Column(Date, nullable=False)
    tipo = Column(String, nullable=False)  # ENTRADA / SALIDA
    cantidad = Column(Integer, nullable=False)
