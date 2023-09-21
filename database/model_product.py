from sqlalchemy import Column, Integer, String, Decimal, ForeignKey
from sqlalchemy.orm import relationship


class Producto(Base):
    __tablename__ = 'productos'

    id_producto = Column(Integer, primary_key=True, autoincrement=True) #pk id
    nombre_producto = Column(String(20), nullable=False, unique=True)
    peso_producto = Column(String(10))
    unidades_producto = Column(String(5), nullable=False)
    precio_venta = Column(Decimal(10, 2), nullable=False)
    precio_real = Column(Decimal(10, 2), nullable=False)
    descripcion = Column(String(3000), nullable=False)
    id_user = Column(Integer, ForeignKey('usuarios.id_user'))
    usuario = relationship("User", back_populates="productos")
