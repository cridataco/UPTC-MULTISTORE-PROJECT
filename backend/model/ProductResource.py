from sqlalchemy import Column, Integer, Float, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class ProductResource(Base):
    __tablename__ = "product_resources"

    id = Column(Integer, primary_key=True, autoincrement=True)
    product_length = Column(Float, nullable=False)
    product_width = Column(Float, nullable=False)
    product_height = Column(Float, nullable=False)
    product_weight = Column(Float, nullable=False)
    product_dimension = Column(String, nullable=False)

    product_id = Column(Integer, ForeignKey("products.id"))

    product = relationship("Product", back_populates="product_resources")

    product_url_resources = relationship("ProductURLResource", back_populates="product_resource")

    def product_volume(self):
        return self.product_length * self.product_width * self.product_height

    def product_density(self):
        return self.product_weight / self.product_volume()


class ProductURLResource(Base):
    __tablename__ = "product_url_resources"

    id = Column(Integer, primary_key=True, autoincrement=True)
    url = Column(String, nullable=False)
    product_resource_id = Column(Integer, ForeignKey("product_resources.id"))

    product_resource = relationship("ProductResource", back_populates="product_url_resources")
