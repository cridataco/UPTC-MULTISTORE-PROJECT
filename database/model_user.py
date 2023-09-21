from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

engine = create_engine('conexion bd')
Session = sessionmaker(bind=engine)

class User(Base):
    __tablename__ = 'usuarios'

    id_user = Column(Integer(), primary_key=True, autoincrement=True)
    id_plataforma = Column(String(15), nullable=False, unique=True)
    correo_electronico = Column(String(100), nullable=False, unique=True)
    contrasena_cuenta = Column(String(50), nullable=False)
    nombre_usuario = Column(String(30), nullable=False, unique=True)


Base.metadata.create_all(engine)