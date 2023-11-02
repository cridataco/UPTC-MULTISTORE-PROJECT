from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date, create_engine
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()

# engine = create_engine('conexion bd')
# Session = sessionmaker(bind=engine)
#TODO: hacer engine -----> 
engine = create_engine('tu_conexion_bd')

class User(Base):
    __tablename__ = 'users'

    id_user = Column(Integer, primary_key=True, autoincrement=True)
    id_platform = Column(String(15), nullable=False, unique=True)
    email = Column(String(100), nullable=False, unique=True)
    user_name = Column(String(30), nullable=False)
    birthdate = Column(Date, nullable=False)
    document_number = Column(String(11), nullable=False, unique=True)
    document_type = Column(Integer, nullable=False)
    is_client = Column(Integer, nullable=False)
    cell_phone_number = Column(String(10), nullable=False)
    user_rol = Column(String(7), nullable=False)
    user_permissions = Column(String(7), nullable=False)
    date_account_deletion = Column(Date, nullable=False)
    date_account_creation = Column(Date,nullable=True)
    
    shipping_address = relationship("ShippingAddress")
    orders = relationship("Orders")

    def getOlderUserCreated(self):
        with engine.connect() as connection:
            result = connection.execute('''
                SELECT * FROM users
                ORDER BY date_account_creation DESC
                LIMIT 1;
            ''')
        return result.fetchone()
        
    



    #zzzzz

# Base.metadata.create_all(engine)
