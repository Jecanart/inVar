from sqlalchemy import Column, Integer, Date, Numeric, String
from app.database import Base

class Compra(Base):
    __tablename__ = "compra"

    id = Column(Integer, primary_key=True, index=True)
    fecha = Column(Date, nullable=False)
    total = Column(Numeric(12, 2), nullable=False)
    proveedor = Column(String, nullable=False)
