from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.sql_base import Base
from config import DB_URI

#Imports para cargar el modelo
from models.categories import Categories
from models.classification import Classification
from models.coupons import Coupons
from models.features import Features
from models.order_details import OrderDetails
from models.orders import Orders
from models.places import Places
from models.price_history import PriceHistory
from models.product_features import ProductFeatures
from models.product_stock import ProductStock
from models.product import Product
from models.ratings import Ratings
from models.resources import Resources
from models.shipping_address import ShippingAddress
from models.taxes import Taxes
from models.user import User

# Crear el motor a la base de datos MySQL
engine = create_engine(DB_URI)

# Crear todas las tablas definidas en el modelo
Base.metadata.create_all(engine)

# Crear una sesion
Session = sessionmaker(bind=engine)
session = Session()
