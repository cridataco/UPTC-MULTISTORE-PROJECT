from sqlalchemy import Column, String, Integer, Float
from sqlalchemy.orm import declarative_base

from backend.model.ConnectDB import ConnectionDB

Base = declarative_base()


class Product(Base):
    __tablename__ = "products"
    id_ = Column(Integer, primary_key=True, nullable=False, unique=True)
    name_product = Column(String(50), nullable=False)
    original_price = Column(Float, nullable=False)
    discount = Column(Float, nullable=False)
    discounted_price = Column(Float, nullable=False)
    description_product = Column(String(1000), nullable=False)
    image_url = Column(String(1000), nullable=False)
    category = Column(String(50), nullable=False)
    stock = Column(Integer, nullable=False)
    stars = Column(Float, nullable=False)

    def __init__(self, id_, name_product, original_price, description_product, image_url, category):
        self.id_ = id_
        self.name_product = name_product
        self.original_price = original_price
        self.discount = 0
        self.discounted_price = original_price
        self.description_product = description_product
        self.image_url = image_url  # no / se debe crear una tabla de imagenes
        self.category = category
        self.stock = 0
        self.stars = 0  # no
        # coments Se debe crear nueva tabla y enlazar con la tabla de productos

    def __str__(self):
        return (f"Product: {self.name_product} \n"
                f"Price: {self.original_price} \n"
                f"Description: {self.description_product} \n"
                f"Image: {self.image_url} \n"
                f"Category: {self.category} \n"
                f"Stock: {self.stock} \n"
                f"Stars: {self.stars} \n")

    @classmethod
    def add_product(cls, id_, name_product, original_price, description_product, image_url, category, db_url):
        # Crear una instancia de ConnectionDB y obtener una sesión
        db = ConnectionDB(db_url)
        session = db.Session()
        try:
            # Verificar si ya existe un producto con el mismo id_
            existing_product = session.query(cls).filter_by(id_=id_).first()
            if existing_product:
                return False  # Ya existe un producto con el mismo id_
            # Crear una nueva instancia de Producto y agregarla a la sesión
            product = cls(
                id_=id_,
                name_product=name_product,
                original_price=original_price,
                description_product=description_product,
                image_url=image_url,
                category=category
            )
            session.add(product)
            session.commit()
            return True  # Producto agregado con éxito
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()

    @classmethod
    def delete_product(cls, id_, db_url):
        db = ConnectionDB(db_url)
        session = db.Session()
        try:
            # Verificar si ya existe un producto con el mismo id_
            existing_product = session.query(cls).filter_by(id_=id_).first()
            if existing_product:
                session.delete(existing_product)
                session.commit()
                return True  # Producto eliminado con éxito
            else:
                return False  # No existe un producto con el mismo id_
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()

    @classmethod
    def update_Description(cls, id_, description_product, db_url):
        db = ConnectionDB(db_url)
        session = db.Session()
        try:
            # Verificar si ya existe un producto con el mismo id_
            existing_product = session.query(cls).filter_by(id_=id_).first()
            if existing_product:
                existing_product.description_product = description_product
                session.commit()
                return True  # Producto actualizado con éxito
            else:
                return False  # No existe un producto con el mismo id_
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()

    @classmethod
    def update_Stock(cls, id_, stock, db_url):
        db = ConnectionDB(db_url)
        session = db.Session()
        try:
            # Verificar si ya existe un producto con el mismo id_
            existing_product = session.query(cls).filter_by(id_=id_).first()
            if existing_product:
                existing_product.stock = stock
                session.commit()
                return True  # Producto actualizado con éxito
            else:
                return False  # No existe un producto con el mismo id_
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()

    @classmethod
    def apply_discount(cls, id_, discount, db_url):
        db = ConnectionDB(db_url)
        session = db.Session()
        try:
            # Verificar si ya existe un producto con el mismo id_
            existing_product = session.query(cls).filter_by(id_=id_).first()
            if existing_product:
                existing_product.discount = discount
                existing_product.discounted_price = existing_product.original_price * ((100 - discount) / 100)
                session.commit()
                return True  # Producto actualizado con éxito
            else:
                return False  # No existe un producto con el mismo id_
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()

    @classmethod
    def update_price(cls, id_, newprice, db_url):
        db = ConnectionDB(db_url)
        session = db.Session()
        try:
            # Verificar si ya existe un producto con el mismo id_
            existing_product = session.query(cls).filter_by(id_=id_).first()
            if existing_product:
                existing_product.original_price = newprice
                session.commit()
                return True  # Producto actualizado con éxito
            else:
                return False  # No existe un producto con el mismo id_
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()

    @classmethod
    def update_category(cls, id_, category, db_url):
        db = ConnectionDB(db_url)
        session = db.Session()
        try:
            # Verificar si ya existe un producto con el mismo id_
            existing_product = session.query(cls).filter_by(id_=id_).first()
            if existing_product:
                existing_product.category = category
                session.commit()
                return True  # Producto actualizado con éxito
            else:
                return False  # No existe un producto con el mismo id_
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()
