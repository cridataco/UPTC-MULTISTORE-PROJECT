from sqlalchemy import Column, Integer, String, ForeignKey, text
from sqlalchemy.orm import relationship
from sqlalchemy.orm.session import Session
from sqlalchemy.exc import NoResultFound
from .sql_base import Base

class Places(Base):
    __tablename__ = "places"

    id_place = Column(Integer, primary_key=True, autoincrement=True)  # pk id
    id_location = Column(
        Integer, ForeignKey("places.id_place"), nullable=True, autoincrement=True
    )  # fk places
    place_name = Column(String(50), nullable=False)
    place_type = Column(String(7), nullable=False)
    postal_code = Column(Integer, nullable=False)

    # One place can have Many sub-places
    sub_places = relationship("Places", back_populates="places", remote_side=[id_place])
    # Many sub-places can have Many places
    places = relationship("Places", back_populates="sub_places")
    # One place can have Many shipping addresses ????
    shipping_addresses = relationship("ShippingAddress", back_populates="place")
    
    def __init__(self, place_name, place_type, postal_code):
        self.place_name = place_name
        self.place_type = place_type
        self.postal_code = postal_code

    #Query para crear lugares
    def create_places(cls, session):
        session.add(cls)
        session.commit()
        return cls     

    #Query para obtener el lugar que más pedidos tiene
    def getOlderCouponCreated(self, engine):
        with engine.connect() as connection:
            result = connection.execute(
                text("SELECT places.id_place, places.place_name, COUNT(orders.id_order) AS quantity_orders FROM places INNER JOIN direcciones ON places.id_place = shipping_address.id_place INNER JOIN users ON shipping_address.id_user = users.id_user INNER JOIN orders ON users.id_user = orders.id_user GROUP BY places.id_place, places.place_name ORDER BY quantity_orders DESC LIMIT 1;")
            )
        return result.fetchone()    

    #Query para obtener el total de lugares
    def getTotalCoupons(self, engine):
        with engine.connect() as connection:
            result = connection.execute(
                text("SELECT COUNT(id_place) FROM coupons;")
            )
        return result.fetchone()  

    #Query para obtener el lugar con más direcciones de envio
    def getRestrictionCupon(self, engine):
        with engine.connect() as connection:
            result = connection.execute(
                text("SELECT places.id_place, places.place_name, COUNT(shipping_address.id_address) AS quantity_address FROM places INNER JOIN shipping_address ON places.id_place = shipping_address.id_place GROUP BY places.id_place, places.place_name ORDER BY quantity_address DESC LIMIT 1;")
            )
        return result.fetchone()  

    #Query para borrar lugar
    def deletePlace(session : Session, id_place):
        try:
            obj_to_del = session.query(Places).filter_by(id_place=id_place).one()
            session.delete(obj_to_del)
            session.commit()
            return True
        except NoResultFound:
            return False    