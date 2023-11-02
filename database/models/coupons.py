from sqlalchemy import Column, Integer, String, Numeric, Date, text
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

    def __init__(
        self,
        coupon_code,
        discount,
        creation_date,
        redeeming_date,
        due_date,
        restrictions,
    ):
        self.coupon_code = coupon_code
        self.discount = discount
        self.creation_date = creation_date
        self.redeeming_date = redeeming_date
        self.due_date = due_date
        self.restrictions = restrictions

    def create_cupon(cls, session):
        session.add(cls)
        session.commit()
        return cls    

    def getOlderCouponCreated(self, engine):
        with engine.connect() as connection:
            result = connection.execute(
                text("SELECT id_coupon, coupon_code FROM coupons ORDER BY creation_date ASC LIMIT 1;")
            )
        return result.fetchone() 

    def getOlderCouponDue(self, engine):
        with engine.connect() as connection:
            result = connection.execute(
                text("SELECT id_coupon, coupon_code FROM coupons ORDER BY due_date ASC LIMIT 1;")
            )
        return result.fetchone()     

    def getTotalCoupons(self, engine):
        with engine.connect() as connection:
            result = connection.execute(
                text("SELECT COUNT(id_coupon) FROM coupons;")
            )
        return result.fetchone()  

    def getRestrictionCupon(self, engine, id_coupon):
        with engine.connect() as connection:
            result = connection.execute(
                text("SELECT restrictions FROM coupons WHERE id_coupon = :id_coupon"), id_coupon = id_coupon
            )
        return result.fetchone()  


    def getSpecifiedCouponByCreationDate(self, engine, due_date):
        with engine.connect() as connection:
            result = connection.execute(
                text("SELECT id_coupon, coupon_code FROM coupons WHERE due_date = :date"), due_date = due_date
            )
        return result.fetchone()             

    def getCouponWithDiscount(self, engine):
        with engine.connect() as connection:
            result = connection.execute(
                text("SELECT id_coupon, coupon_code FROM coupons WHERE discount IS NOT NULL;")
            )
        return result.fetchone() 

    def getCouponWithoutDiscount(self, engine):
        with engine.connect() as connection:
            result = connection.execute(
                text("SELECT id_coupon, coupon_code FROM coupons WHERE discount IS NULL;")
            )
        return result.fetchone()     