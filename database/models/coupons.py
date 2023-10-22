from sqlalchemy import Column, Integer, String, Numeric, Date
from sqlalchemy.orm import relationship
from .sql_base import Base


class Coupons(Base):
    __tablename__ = "coupons"

    id_coupon = Column(Integer, primary_key=True, autoincrement=True)  # pk id
    coupon_code = Column(String(10), nullable=False)
    discount = Column(Numeric(precision=12, scale=2), nullable=False)
    creation_date = Column(Date, nullable=False)  # Fecha de creacion del cupon
    redeeming_date = Column(Date, nullable=False)
    due_date = Column(Date, nullable=False)  # Fecha de vencimiento
    restrictions = Column(String(100), nullable=False)
    # La fecha de creacion debe ser menor a la fecha de vencimiento

    # One coupon can be used for Many orders
    orders = relationship("Orders", back_populates="coupon")
