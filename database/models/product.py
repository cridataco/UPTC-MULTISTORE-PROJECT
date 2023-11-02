from sqlalchemy import Column, Integer, String, Date, ForeignKey, text
from sqlalchemy.orm import relationship
from sqlalchemy.orm.session import Session
from .sql_base import Base


class Product(Base):
    __tablename__ = "product"

    id_product = Column(Integer, primary_key=True, autoincrement=True)  # pk id
    id_tax = Column(Integer, ForeignKey("taxes.id_tax"), nullable=False)  # fk taxes
    product_name = Column(String(50), nullable=False)
    reference_model = Column(String(50), nullable=False)
    summary_description = Column(String(100), nullable=False)
    release_date = Column(Date, nullable=False)
    creation_date = Column(Date, nullable=False)
    key_words = Column(String(100), nullable=True)
    product_link = Column(String(500), nullable=True)

    # Many products can have One tax
    tax = relationship("Taxes", back_populates="products")
    # One product can have Many resources
    resources = relationship("Resources", back_populates="product")
    classifications = relationship("Classification")
    product_stock = relationship("ProductStock")
    price_history = relationship("PriceHistory")
    ratings = relationship("Ratings")
    product_features = relationship("ProductFeatures")

    def __init__(
        self,
        product_name,
        reference_model,
        summary_description,
        release_date,
        creation_date,
        key_words=None,
        product_link=None,
    ):
        self.product_name = product_name
        self.reference_model = reference_model
        self.summary_description = summary_description
        self.release_date = release_date
        self.creation_date = creation_date
        self.key_words = key_words
        self.product_link = product_link

    def create_product(cls, session):
        session.add(cls)
        session.commit()
        return cls
    
    #Query Delete Porduct
    def deleteUser(session: Session, id_product):
        try:
            obj_to_del = session.query(Product), filter_by(id_product = id_product).one()
            session.detele(obj_to_del)
            session.commit()
            return True
        except NoResultFound:
            return False

    def getTotalProducts(self, engine):
        with engine.connect() as connection:
            result = connection.execute(
                text("SELECT COUNT(*) FROM product;")
            )
        return result.fetchone()

    def getOlderProductCreated(self, engine):
        with engine.connect() as connection:
            result = connection.execute(
                text("SELECT * FROM product ORDER BY creation_date ASC LIMIT 1;")
            )
        return result.fetchone()

    def getNewestProductCreated(self, engine):
        with engine.connect() as connection:
            result = connection.execute(
                text("SELECT * FROM product ORDER BY creation_date DESC LIMIT 1;")
            )
        return result.fetchone()

    def getOlderProductReleased(self, engine):
        with engine.connect() as connection:
            result = connection.execute(
                text("SELECT * FROM product ORDER BY released_date ASC LIMIT 1;")
            )
        return result.fetchone()

    def getNewestProductReleased(self, engine):
        with engine.connect() as connection:
            result = connection.execute(
                text("SELECT * FROM product ORDER BY released_date DESC LIMIT 1;")
            )
        return result.fetchone()

    def getSpecifiedProductByName(self, engine, productName):
        with engine.connect() as connection:
            result = connection.execute(
                text("SELECT * FROM product WHERE product_name = :productName"), productName = productName
            )
        return result.fetchone()
