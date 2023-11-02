from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.sql_base import Base
from models import (
    categories,
    classification,
    coupons,
    features,
    order_details,
    orders,
    places,
    price_history,
    product_features,
    product_stock,
    product,
    ratings,
    resources,
    shipping_address,
    taxes,
    user,
)


# Crear el motor a la base de datos MySQL
database_uri = "URI MySQL bd"  # URI propia
engine = create_engine(database_uri)

# Crear todas las tablas definidas en el modelo
Base.metadata.create_all(engine)

# Crear una sesion
Session = sessionmaker(bind=engine)
session = Session()
# Consultas

"""
#taxes.Taxes.create_tax(session=session, tax_value=10)
tax_readed : taxes.Taxes= taxes.Taxes.read_tax(session=session,tax_id=1)
print(f"ID: {tax_readed.id_tax} - Valor: {tax_readed.tax_value}")
"""
men= user.User(
    id_platform="as",
    email="correo",
    user_name="nombre",
    birthdate= "2001-12-11",
    document_number="numero",
    document_type=1,
    is_client=2,
    cell_phone_number="as",
    user_rol="asd",
    user_permissions="admin",
    date_account_creation="2001-12-11"
)

user.User.create_user(cls=men, session=session)


# Cerrar la sesión
session.close()
