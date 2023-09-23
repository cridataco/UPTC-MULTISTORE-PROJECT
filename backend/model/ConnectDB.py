from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Product import Product, Base


class ConnectionDB:
    def __init__(self, db_url):
        self.engine = create_engine(db_url)
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)

    def create_Product(self, product):
        session = self.Session()
        try:
            existing_Product = session.query(Product).filter_by(name=product.name,
                                                                description=product.description).first()
            if existing_Product:
                return False
            session.add(product)
            session.commit()
            return True
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()

    def update_price(self, product_id, new_price):
        session = self.Session()
        try:
            product = session.query(Product).filter_by(id_=product_id).first()
            if product:
                product.modify_price(new_price)
                session.commit()
                return True
            else:
                return False
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()

    def update_discount(self, product_id, new_discount):
        session = self.Session()
        try:
            product = session.query(Product).filter_by(id_=product_id).first()
            if product:
                product.modify_discount(new_discount)
                session.commit()
                return True
            else:
                return False
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()

    def update_description(self, product_id, new_description):
        session = self.Session()
        try:
            product = session.query(Product).filter_by(id_=product_id).first()
            if product:
                product.modify_description(new_description)
                session.commit()
                return True
            else:
                return False
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()

    def delete_Product(self, product_id):
        session = self.Session()
        try:
            product = session.query(Product).filter_by(id_=product_id).first()
            if product:
                session.delete(product)
                session.commit()
                return True
            else:
                return False
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()

    def show_Products(self):
        session = self.Session()
        try:
            products = session.query(Product).all()
            return products
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()

