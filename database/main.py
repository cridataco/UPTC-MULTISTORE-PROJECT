from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.sql_base import Base
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
from queries import q_user

# Crear el motor a la base de datos MySQL
database_uri = "mysql://root:sebas123rt@127.0.0.1/test_project_db"  # URI
engine = create_engine(database_uri)

# Crear todas las tablas definidas en el modelo
Base.metadata.create_all(engine)

# Crear una sesion
Session = sessionmaker(bind=engine)
session = Session()
# Consultas

men= User(
    id_platform="451",
    email="hector4@gmail.com",
    user_name="Hector",
    birthdate= "2004-04-11",
    document_number="105555555",
    document_type=2,
    is_client=2,
    cell_phone_number="31000000",
    user_rol="cliente",
    user_permissions="cliente",
    date_account_creation="2023-11-03"
)
men2= User(
    id_platform="lols",
    email="rakan@lg.co",
    user_name="rakan1",
    birthdate= "2004-12-13",
    document_number="1231231",
    document_type=2,
    is_client=1,
    cell_phone_number="60010060",
    user_rol="admin",
    user_permissions="admin",
    date_account_creation="2023-08-11"
)
# Create user
#q_user.createUser(session=session, user=men)
#q_user.createUser(session=session, user=men2)

# Get User
#print(q_user.getByIdUser(session=session, id_user=20))

# Delete user
#print(q_user.deleteUser(session=session, id_user=14))

# Cerrar la sesión
session.close()
