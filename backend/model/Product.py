from sqlalchemy import Column, String, Integer, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Product(Base):
    __tablename__ = "products"
    id_ = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    price = Column(Float, nullable=False)
    discount = Column(Float, nullable=False)
    description = Column(String(1000), nullable=False)
    image = Column(String(1000), nullable=False)
    category = Column(String(50), nullable=False)
    quantity = Column(Integer, nullable=False)
    stars = Column(Float, nullable=False)

    def __init__(self, name, price, description, image, category, quantity):
        self.name = name
        self.price = price
        self.discount = 0
        self.description = description
        self.image = image
        self.category = category
        self.quantity = quantity
        self.stars = 0

    def __str__(self):
        return (
            f"--> Product: {self.name}\n"
            f"    Price: {self.price}\n"
            f"    Discount: {self.discount}\n"
            f"    Category: {self.category}\n"
            f"    Quantity: {self.quantity}\n"
            f"    Description: {self.description}\n"
        )

    def modify_price(self, price):
        if price > 0:
            self.price = price
            return True
        else:
            return False

    def modify_discount(self, discount):
        if 0 <= discount <= 100:
            self.discount = discount
            return True
        else:
            return False

    def modify_description(self, description):
        self.description = description
        return True

    def modify_image(self, image):
        self.image = image
        return True

    def update_Stars(self, stars):
        if stars > 0:
            self.stars = stars
            return True
        else:
            return False
