from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from .sql_base import Base


class Classification(Base):
    __tablename__ = "classification"

    id_product = Column(
        Integer, ForeignKey("product.id_product"), primary_key=True, nullable=False
    )  # fk product
    id_category = Column(
        Integer, ForeignKey("categories.id_category"), primary_key=True, nullable=False
    )  # fk categories

    # Intermediate relationship: Many products have Many categories
    category = relationship("Categories", back_populates="classifications")
    product = relationship("Product", back_populates="classifications")
