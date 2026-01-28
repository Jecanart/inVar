from sqlalchemy import Column, Integer, Date, Numeric
from app.database import Base

class Venta(Base):
    __tablename__ = "ventas"

    id = Column(Integer, primary_key=True, index=True)
    fecha = Column(Date, nullable=False)
    total = Column(Numeric(12, 2), nullable=False)
