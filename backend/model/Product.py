from sqlalchemy import Column, String, Integer, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from backend.model.ConnectDB import ConnectionDB
from backend.model.test import db_url

Base = declarative_base()


class Product(Base):

    def __init__(self, id_product, name_product, reference_model, product_features, keywords, product_resource,
                 product_category, product_rating, price_actual, product_stock, product_tax, image_url):
        self.id_ = id_product
        self.name_product = name_product
        self.reference_mocel = reference_model
        self.product_features = product_features
        self.keywords = keywords
        self.product_resource = product_resource
        self.product_category = product_category
        self.product_rating = product_rating
        self.price_actual = price_actual
        self.current_product_stock = product_stock
        self.product_tax = product_tax
        self.image_url = image_url  # no / se debe crear una tabla de imagenes
        self.stars_rating = 0  # no
        # coments Se debe crear nueva tabla y enlazar con la tabla de productos



    __tablename__ = "products"
    id_product = Column(Integer, primary_key=True, nullable=False, unique=True)
    name_product = Column(String(50), nullable=False)
    price_actual = Column(Float, nullable=False)
    discount = Column(Float, nullable=False)
    discounted_price = Column(Float, nullable=False)
    description_product = Column(String(1000), nullable=False)
    image_url = Column(String(1000), nullable=False)
    product_category = Column(String(50), nullable=False)
    current_product_stock = Column(Integer, nullable=False)
    stars_rating = Column(Float, nullable=False)


    def __str__(self):
        return (f"Product: {self.name_product} \n"
                f"Price: {self.price_actual} \n"
                f"Description: {self.product_features} \n"
                f"Image: {self.image_url} \n"
                f"Category: {self.product_category} \n"
                f"Stock: {self.current_product_stock} \n"
                f"Stars: {self.stars_rating} \n")

    @classmethod
    def add_product(cls,  id_product, name_product, reference_model, product_features, keywords, product_resource,
                 product_category, product_rating, price_actual, product_stock, product_tax, image_url):
        # Crear una instancia de ConnectionDB y obtener una sesión
        db = ConnectionDB(db_url)
        session = db.Session()
        try:
            # Verificar si ya existe un producto con el mismo id_
            existing_product = session.query(cls).filter_by(id_= id_product).first()
            if existing_product:
                return False  # Ya existe un producto con el mismo id_
            # Crear una nueva instancia de Producto y agregarla a la sesión
            product = cls(
                id_= id_product,
                name_product=name_product,
                reference_model = reference_model,
                product_features = product_features,
                keywords = keywords,
                product_resource= product_resource,
                product_category=product_category,
                product_rating= product_rating,
                price_actual = price_actual,
                product_stock = product_stock,
                product_tax = product_tax,
                image_url=image_url,
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
    def delete_product(cls, id_product, db_url):
        db = ConnectionDB(db_url)
        session = db.Session()
        try:
            # Verificar si ya existe un producto con el mismo id_
            existing_product = session.query(cls).filter_by(id_=id_product ).first()
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
    def update_Description(cls, id_product, product_features, db_url):
        db = ConnectionDB(db_url)
        session = db.Session()
        try:
            # Verificar si ya existe un producto con el mismo id_
            existing_product = session.query(cls).filter_by(id_= id_product).first()
            if existing_product:
                existing_product.product_features = product_features
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
    def update_Stock(cls, id_product, current_product_stock, db_url):
        db = ConnectionDB(db_url)
        session = db.Session()
        try:
            # Verificar si ya existe un producto con el mismo id_
            existing_product = session.query(cls).filter_by(id_product= id_product).first()
            if existing_product:
                existing_product.stock = current_product_stock
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
    def apply_discount(cls, id_product, discount, db_url):
        db = ConnectionDB(db_url)
        session = db.Session()
        try:
            # Verificar si ya existe un producto con el mismo id_
            existing_product = session.query(cls).filter_by(id_=id_product).first()
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
    def update_price(cls, id_product, newprice, db_url):
        db = ConnectionDB(db_url)
        session = db.Session()
        try:
            # Verificar si ya existe un producto con el mismo id_
            existing_product = session.query(cls).filter_by(id_=id_product).first()
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
    def update_category(cls, id_product, category, db_url):
        db = ConnectionDB(db_url)
        session = db.Session()
        try:
            # Verificar si ya existe un producto con el mismo id_
            existing_product = session.query(cls).filter_by(id_=id_product).first()
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

    def obtener_videos_y_fotos(self):
        # Crear una instancia de ConnectionDB y obtener una sesión
        db = ConnectionDB(db_url)
        Session = sessionmaker(bind=db.engine)
        session = Session()

        try:
            # Consultar la base de datos para obtener video_url y foto_url
            result = session.query(Product.video_url, Product.foto_url).filter_by(id_=self.id_).first()

            if result:
                video_url, foto_url = result
                videos_fotos = {
                    'video_url': video_url,
                    'foto_url': foto_url
                }
                return videos_fotos
            else:
                return {}

        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()
