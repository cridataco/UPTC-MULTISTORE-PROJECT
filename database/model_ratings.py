from sqlalchemy import Column, String, Integer, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Ratings(Base):
    __tablename__ = "ratings"

    id_order = Column(
        Integer, ForeignKey("orders.id_order"), primary_key=True, nullable=False
    )  # fk orders
    id_product = Column(
        Integer, ForeignKey("product.id_product"), primary_key=True, nullable=False
    )  # fk product
    rating = Column(Integer, nullable=False)
    comment = Column(String(1000), nullable=False)
    rating_date = Column(Date, nullable=False)
    rating_edit_date = Column(Date, nullable=True)
    rating_elimination_date = Column(Date, nullable=False)
