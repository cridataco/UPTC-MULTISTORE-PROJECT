from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date, Boolean, create_engine
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
    fecha_nacimiento = Column(Date)
    numero_documento = Column(String(12), nullable=False, unique=True)
    tipo_documento = Column(Integer(10), nullable=False, unique=True)
    
    es_vendedor = Column(Boolean)
    numero_celular = Column(String(1024))


Base.metadata.create_all(engine)