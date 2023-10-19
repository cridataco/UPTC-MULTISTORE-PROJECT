from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class ProductFeatures(Base):
    __tablename__ = "product_features"

    id_product = Column(
        Integer, ForeignKey("product.id_product"), primary_key=True, nullable=False
    )  # fk product
    id_feature = Column(
        Integer, ForeignKey("features.id_feature"), primary_key=True, nullable=False
    )  # fk features
    feature_value = Column(String(30), nullable=True)
