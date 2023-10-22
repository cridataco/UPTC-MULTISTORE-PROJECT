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

# Consulta con User
# Va a dar error, porque la tabla esta vacia, y aún no hay consulta para agregar un nuevo usuario
"""
user_test = user.User()
user_test.getOlderUserCreated(engine)
"""

# Cerrar la sesión
session.close()
