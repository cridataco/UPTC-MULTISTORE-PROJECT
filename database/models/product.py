from sqlalchemy import Column, Integer, String, Date, ForeignKey, text
from sqlalchemy.orm import relationship
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
    
    # Query to get product with the highest price 
    def getProductWithHighestActualPrice(self, engine):
        with engine.connect() as connection:
            result = connection.execute(
                text("""SELECT product_name FROM product p, price_history ph
                        WHERE p.id_product = ph.id_product
                        ORDER BY ph.purchase_price
                        DCS LIMIT 1;""")
            )
        return result.fetchone()
    
    # Query to get product with the Lowest price 
    def getProductWithLowestActualPrice(self, engine):
        with engine.connect() as connection:
            result = connection.execute(
                text("""SELECT product_name FROM product p, price_history ph
                        WHERE p.id_product = ph.id_product
                        ORDER BY ph.purchase_price
                        ACS LIMIT 1;""")
            )
        return result.fetchone()
    
    # Get products with the highest rating
    def getProductsWithLowestRating(self, engine):
        with engine.connect() as connection:
            result = connection.execute(
                text("""SELECT p.PRODUCT_NAME, AVG(r.RATING) AS AVG_RATING
                            FROM PRODUCT p, RATINGS r
                            WHERE p.ID_PRODUCT = r.ID_PRODUCT
                            GROUP BY p.PRODUCT_NAME
                            ORDER BY AVG_RATING DESC
                            LIMIT 1;
                            """)
            )
        return result.fetchone()
    
    # Get products with the lowest rating
    def getProductsWithLowestRating(self, engine):
        with engine.connect() as connection:
            result = connection.execute(
                text("""SELECT p.PRODUCT_NAME, AVG(r.RATING) AS AVG_RATING
                            FROM PRODUCT p, RATINGS r
                            WHERE p.ID_PRODUCT = r.ID_PRODUCT
                            GROUP BY p.PRODUCT_NAME
                            ORDER BY AVG_RATING ACS
                            LIMIT 1;""")
            )
        return result.fetchone()
    
    #Query to get the most purchased product for all time
    #TODO: add query
    def getBestSellerProduct(self, engine):
        with engine.connect() as connection:
            result = connection.execute(
                text("""SELECT product_name, (SELECT SUM(od. quantity) 
                                            FROM order_details od) AS TOTAL
                        FROM product p, orders o, order_details od, stock s
                        where p.id_product = od.id_product
                        and od.id_order = o.id_order
                        and od.id_stock = s.id_stock
                        GROUP BY p.PRODUCT_NAME
                        ORDER BY TOTAL DESC
                        LIMIT 1;""")
            )
        return result.fetchone()
    
    #producto con mas impuestos
    def getProductWithHighestTaxes(self, engine):
        with engine.connect() as connection:
            result = connection.execute(
                text("""SELECT product_name FROM product p, taxes t
                        WHERE p.id_tax = t.id_tax
                        AND t.tax = (SELECT MAX(tax) 
                                        FROM taxes);""")
            )
        return result.fetchone()
    
    #producto con mas impuestos
    def getProductWithLowestTaxes(self, engine):
        with engine.connect() as connection:
            result = connection.execute(
                text("""SELECT product_name FROM product p, taxes t
                        WHERE p.id_tax = t.id_tax
                        AND t.tax = (SELECT MAX(tax) 
                                        FROM taxes);""")
            )
        return result.fetchone()