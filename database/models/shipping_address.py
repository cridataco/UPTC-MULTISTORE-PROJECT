from sqlalchemy import Column, Integer, String, ForeignKey, text
from sqlalchemy.orm import relationship
from sqlalchemy.orm.session import Session
from sqlalchemy.exc import NoResultFound
from .sql_base import Base


class ShippingAddress(Base):
    __tablename__ = "shipping_address"

    id_address = Column(Integer, primary_key=True, autoincrement=True)  # pk id
    id_user = Column(Integer, ForeignKey("users.id_user"), nullable=False)  # fk users
    id_place = Column(
        Integer, ForeignKey("places.id_place"), nullable=True
    )  # fk places
    shipping_address = Column(String(100), nullable=False)
    shipment_receiver_name = Column(String(30), nullable=False)
    receiver_phone = Column(String(10), nullable=True)
    address_details = Column(String(50), nullable=True)

    # Many shipping addresses can be from One place ?????
    place = relationship("Places", back_populates="shipping_addresses")
    # Many shipping addresses can be from One user
    user = relationship("User", back_populates="shipping_addresses")
    orders = relationship("Orders")

    def __init__(
        self,
        shipping_address,
        shipment_receiver_name,
        receiver_phone=None,
        address_details=None,
    ):
        self.shipping_address = shipping_address
        self.shipment_receiver_name = shipment_receiver_name
        self.receiver_phone = receiver_phone
        self.address_details = address_details

    #Query para crear direccion de envio
    def create_shipping_address(cls, session):
        session.add(cls)
        session.commit()
        return cls    

    #Query para obtener la direccion del id de un usuario en especifico
    def getAddresUser(self, engine, id_user):
        with engine.connect() as connection:
            result = connection.execute(
                text("SELECT id_addres FROM shipping_address WHERE id_user = :id_user;"), id_user = id_user
            )
        return result.fetchone() 
    
    #Query para obtener los datos del usuario de un pedido en especifico
    def getAddresUser(self, engine, id_order):
        with engine.connect() as connection:
            result = connection.execute(
                text
                ("SELECT users.user_name, shipping_address, shipment_receiver_name, receiver_phone FROM shipping_address INNER JOIN users ON shipping_address.id_user = users.id_user INNER JOIN orders ON users.id_user = orders.user_id WHERE id_order = :id_order"), id_order = id_order
            )
        return result.fetchone() 

    #Query para obtener las direcciones de un lugar en especifico
    def getOlderCouponDue(self, engine, place_name):
        with engine.connect() as connection:
            result = connection.execute(
                text("SELECT shipping_address FROM shipping_address INNER JOIN places ON shipping_address.id_address = places.shipping_address WHERE place_name = :place_name"), place_name = place_name
            )
        return result.fetchone()     

    #Query para obtener el total de direcciones de envio
    def getTotalShippingAddress(self, engine):
        with engine.connect() as connection:
            result = connection.execute(
                text("SELECT COUNT(id_address) FROM shipping_address;")
            )
        return result.fetchone()  

    #Query para borrar direccion de envio
    def deleteUser(session : Session, id_address):
        try:
            obj_to_del = session.query(ShippingAddress).filter_by(id_address=id_address).one()
            session.delete(obj_to_del)
            session.commit()
            return True
        except NoResultFound:
            return False    
