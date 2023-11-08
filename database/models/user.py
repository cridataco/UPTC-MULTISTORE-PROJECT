from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import relationship
from .sql_base import Base

class User(Base):
    __tablename__ = "users"

    id_user = Column(Integer, primary_key=True, autoincrement=True)
    id_platform = Column(String(15), nullable=False, unique=True)
    email = Column(String(100), nullable=False, unique=True)
    user_name = Column(String(30), nullable=False)
    jwt_tokken = Column(String(150), nullable=False, unique=True)
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
        jwt_tokken,
        birthdate,
        document_number,
        document_type,
        is_client,
        cell_phone_number,
        user_rol,
        user_permissions,
        date_account_creation,
        id_user =None,
        date_account_deletion=None
    ):
        self.id_user = id_user
        self.id_platform = id_platform
        self.email = email
        self.user_name = user_name
        self.jwt_tokken = jwt_tokken
        self.birthdate = birthdate
        self.document_number =  document_number
        self.document_type = document_type
        self.is_client = is_client
        self.cell_phone_number = cell_phone_number
        self.user_rol = user_rol
        self.user_permissions = user_permissions
        self.date_account_creation = date_account_creation
        self.date_account_deletion = date_account_deletion


    def printUser(user):
        print(f"User ID: {user.id_user}")
        print(f"Platform ID: {user.id_platform}")
        print(f"Email: {user.email}")
        print(f"User Name: {user.user_name}")
        print(f"Birthdate: {user.birthdate}")
        print(f"Document Number: {user.document_number}")
        print(f"Document Type: {user.document_type}")
        print(f"Is Client: {user.is_client}")
        print(f"Cell Phone Number: {user.cell_phone_number}")
        print(f"User Role: {user.user_rol}")
        print(f"User Permissions: {user.user_permissions}")
        print(f"Date Account Creation: {user.date_account_creation}")