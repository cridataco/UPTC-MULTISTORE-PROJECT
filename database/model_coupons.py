from sqlalchemy import Column, Integer, String, Numeric, Date
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Coupons(Base):
    __tablename__ = "coupons"

    id_coupon = Column(Integer, primary_key=True, autoincrement=True)  # pk id
    coupon_code = Column(String(10), nullable=False)
    discount = Column(Numeric(precision=12, scale=2),  nullable=False)
    creation_date = Column(Date, nullable=False)#Fecha de creacion del cupon
    redeeming_date = Column(Date,nullable=False)
    due_date = Column(Date, nullable=False) #Fecha de vencimiento
    restrictions = Column(String(100), nullable=False)

    #Señores del back: la fecha de creacion debe ser menor a la fecha de vencimiento
    
    orders = relationship("Orders")
    