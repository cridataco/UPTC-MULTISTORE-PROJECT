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
    date_account_deletion = Column(Date, nullable=False)
    date_account_creation = Column(Date, nullable=True)

    shipping_addresses = relationship("ShippingAddress")
    orders = relationship("Orders")

    def getOlderUserCreated(self, engine):
        with engine.connect() as connection:
            result = connection.execute(
                text("SELECT * FROM users ORDER BY date_account_creation ASC LIMIT 1;")
            )
        return result.fetchone()

    def getTotalUsers(self, engine):
        with engine.connect() as connection:
            result = connection.execute(
                text("SELECT COUNT(*) FROM users;")
            )
        return result.fetchone()
    
    def getNewestUser(self, engine):
        with engine.connect() as connection:
            result = connection.execute(
                text("SELECT * FROM users ORDER BY date_account_creation DESC LIMIT 1;")
            )
        return result.fetchone()
    
    def getClientsUsers(self, engine):
        with engine.connect() as connection:
            result = connection.execute(
                text("SELECT * FROM users WHERE is_client = 1;")
            )
        return result.fetchone()
    
    def getSpecifiedUserByUserName(self, engine, username):
        with engine.connect() as connection:
            result =  connection.execute(
                text("SELECT * FROM users WHERE user_name = :username"), username=username
            )
        return result.fetchone()
    
    def getSpecifiedUserByEmail(self, engine, email):
        with engine.connect() as connection:
            result = connection.execute(
                text("SELECT * FROM users WHERE email = :email"), email = email
            )
        return result.fetchone()
    
    #You must ensure that the 'date' parameter is in 'YYYY-MM-DD' format.
    def getSpecifiedUserByCreationDate(self, engine, date):
        with engine.connect() as connection:
            result = connection.execute(
                text("SELECT * FROM users WHERE date_account_creation = :date"), date = date
            )
        return result.fetchone()
