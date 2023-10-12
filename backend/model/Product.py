from datetime import date
from sqlalchemy import Column, Integer, Float, Date, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class PriceHistory(Base):
    __tablename__ = "price_history"

    id_price_history = Column(Integer, primary_key=True, autoincrement=True)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    price_actual = Column(Float, nullable=False)
    product_id = Column(Integer, ForeignKey("products.id_product"))

    product = relationship("Product", back_populates="price_history")

    def display_price_history(self):
        print(f"ID: {self.id_price_history}")
        print(f"Start Date: {self.start_date}")
        print(f"End Date: {self.end_date}")
        print(f"Price Actual: {self.price_actual}")

class Product(Base):
    __tablename__ = "products"

    id_product = Column(Integer, primary_key=True, autoincrement=True)
    name_product = Column(String(100), nullable=False)
    reference_model = Column(String(100), nullable=False)
    release_date = Column(DateTime, nullable=False)
    creation_date = Column(DateTime, default=func.now())
    product_features = Column(String(100), nullable=False)
    keywords = Column(String(100), nullable=False)
    product_link = Column(String(250), nullable=False)

    price_history = relationship("PriceHistory", back_populates="product")


if __name__ == "__main__":
    ph = PriceHistory(start_date=date(2023, 1, 1), end_date=date(2023, 12, 31), price_actual=100.5)
    product = Product(name_product="Example Product", reference_model="ABC123", release_date=date(2023, 1, 1), product_features="Feature 1, Feature 2", keywords="keyword1, keyword2", product_link="https://example.com")

    product.price_history.append(ph)

    ph.display_price_history()
