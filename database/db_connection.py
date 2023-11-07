from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.sql_base import Base
from config import DB_URI

# Crear el motor a la base de datos MySQL
engine = create_engine(DB_URI)

# Crear todas las tablas definidas en el modelo
Base.metadata.create_all(engine)

# Crear una sesion
Session = sessionmaker(bind=engine)
session = Session()
