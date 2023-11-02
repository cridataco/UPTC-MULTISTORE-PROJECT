from sqlalchemy import Column, Integer, String, Date, text
from sqlalchemy.orm import relationship
from .sql_base import Base


class User(Base):
    __tablename__ = "users"

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
    date_account_creation = Column(Date, nullable=False)
    date_account_deletion = Column(Date, nullable=True)

    shipping_addresses = relationship("ShippingAddress")
    orders = relationship("Orders")

    def __init__(
        self,
        id_platform,
        email,
        user_name,
        birthdate,
        document_number,
        document_type,
        is_client,
        cell_phone_number,
        user_rol,
        user_permissions,
        date_account_creation,
        date_account_deletion=None
    ):
        self.id_platform = id_platform
        self.email = email
        self.user_name = user_name
        self.birthdate = birthdate
        self.document_number =  document_number
        self.document_type = document_type
        self.is_client = is_client
        self.cell_phone_number = cell_phone_number
        self.user_rol = user_rol
        self.user_permissions = user_permissions
        self.date_account_creation = date_account_creation
        self.date_account_deletion = date_account_deletion


    # Query Create User
    def create_user(cls, session):
        session.add(cls)
        session.commit()
        return cls

    # Query Select OlderUser
    def getOlderUserCreated(self, engine):
        with engine.connect() as connection:
            result = connection.execute(
                text("SELECT * FROM users ORDER BY date_account_creation ASC LIMIT 1;")
            )
        return result.fetchone()

    # Query Count Users
    def getTotalUsers(self, engine):
        with engine.connect() as connection:
            result = connection.execute(
                text("SELECT COUNT(*) FROM users;")
            )
        return result.fetchone()
    
    # Query Select NewestUser
    def getNewestUser(self, engine):
        with engine.connect() as connection:
            result = connection.execute(
                text("SELECT * FROM users ORDER BY date_account_creation DESC LIMIT 1;")
            )
        return result.fetchone()
    
    # Query Clients Users
    def getClientsUsers(self, engine):
        with engine.connect() as connection:
            result = connection.execute(
                text("SELECT * FROM users WHERE is_client = 1;")
            )
        return result.fetchone()
    
    # Query Select User By username 
    def getSpecifiedUserByUserName(self, engine, username):
        with engine.connect() as connection:
            result =  connection.execute(
                text("SELECT * FROM users WHERE user_name = :username"), username=username
            )
        return result.fetchone()
    
    # Query Select User By email
    def getSpecifiedUserByEmail(self, engine, email):
        with engine.connect() as connection:
            result = connection.execute(
                text("SELECT * FROM users WHERE email = :email"), email = email
            )
        return result.fetchone()
    
    #Query Select User by date_account_creation
    #You must ensure that the 'date' parameter is in 'YYYY-MM-DD' format.
    def getSpecifiedUserByCreationDate(self, engine, date):
        with engine.connect() as connection:
            result = connection.execute(
                text("SELECT * FROM users WHERE date_account_creation = :date"), date = date
            )
        return result.fetchone()
