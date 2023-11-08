from sqlalchemy import text
from sqlalchemy.orm.session import Session
from models.coupons import Coupons


# Query Create Coupon
def createCoupon(session: Session, coupon: Coupons):
    session.add(coupon)
    session.commit()


# Query Select Coupon by id_coupon
def getCouponByIdCoupon(session: Session, id_coupon):
    return session.query(Coupons).filter_by(id_coupon=id_coupon).first()


# Query Select Coupon by coupon_code
def getCouponByCouponCode(session: Session, coupon_code):
    return session.query(Coupons).filter_by(coupon_code=coupon_code).first()


# Query Select coupon por by creation_date
def getSpecifiedCouponByCreationDate(self, engine, due_date):
    with engine.connect() as connection:
        result = connection.execute(
            text(
                "SELECT id_coupon, coupon_code FROM coupons WHERE due_date = :due_date"
            ),
            due_date=due_date,
        )
    return result.fetchone()


# Query Get coupon_code by id_coupon
def getCouponCode(session: Session, id_coupon):
    return session.query(Coupons.coupon_code).filter_by(id_coupon=id_coupon).scalar()


# Query Get discount by id_coupon
def getDiscount(session: Session, id_coupon):
    return session.query(Coupons.discount).filter_by(id_coupon=id_coupon).scalar()


# Query Get creation_date by id_coupon
def getCreationDate(session: Session, id_coupon):
    return session.query(Coupons.creation_date).filter_by(id_coupon=id_coupon).scalar()


# Query Get redeeming_date by id_coupon
def getRedeemingDate(session: Session, id_coupon):
    return session.query(Coupons.redeeming_date).filter_by(id_coupon=id_coupon).scalar()


# Query Get due_date by id_coupon
def getDueDate(session: Session, id_coupon):
    return session.query(Coupons.due_date).filter_by(id_coupon=id_coupon).scalar()


# Query Get restrictions by id_coupon
def getRestrictions(session: Session, id_coupon):
    return session.query(Coupons.restrictions).filter_by(id_coupon=id_coupon).scalar()


# Query Delete Coupon
def deleteCoupon(session: Session, id_coupon):
    coupon_to_delete = getCouponByIdCoupon(session=session, id_coupon=id_coupon)
    if coupon_to_delete:
        session.delete(coupon_to_delete)
        session.commit()
        return True
    else:
        return False


# Query Update coupon_code
def updateCouponCode(session: Session, id_coupon, coupon_code):
    coupon_to_update = getCouponByIdCoupon(session=session, id_coupon=id_coupon)
    if coupon_to_update:
        coupon_to_update.coupon_code = coupon_code
        session.commit()
        return True
    else:
        return False


# Query Update discount
def updateDiscount(session: Session, id_coupon, discount):
    coupon_to_update = getCouponByIdCoupon(session=session, id_coupon=id_coupon)
    if coupon_to_update:
        coupon_to_update.discount = discount
        session.commit()
        return True
    else:
        return False


# Query Update due_date
def updateDueDate(session: Session, id_coupon, due_date):
    coupon_to_update = getCouponByIdCoupon(session=session, id_coupon=id_coupon)
    if coupon_to_update:
        coupon_to_update.due_date = due_date
        session.commit()
        return True
    else:
        return False


# Query Set redeeming_date
def updateRestrictions(session: Session, id_coupon, restrictions):
    coupon_to_update = getCouponByIdCoupon(session=session, id_coupon=id_coupon)
    if coupon_to_update:
        coupon_to_update.restrictions = restrictions
        session.commit()
        return True
    else:
        return False


# Query Select Older coupon created
def getOlderCouponCreated(session: Session):
    query = text(
        """SELECT id_coupon, coupon_code FROM coupons 
                    ORDER BY creation_date 
                    ASC LIMIT 1;"""
    )
    result = session.execute(query)
    return result.fetchone()


# Query para obtener el primer cupon vencido (el más viejo)
def getOlderCouponDue(session: Session):
    query = text(
        """SELECT id_coupon, coupon_code FROM coupons 
                    ORDER BY due_date 
                    ASC LIMIT 1;"""
    )
    result = session.execute(query)
    return result.fetchone()


# Query para obtener el total de cupones
def getTotalCoupons(session: Session):
    return session.query(Coupons.id_coupon).count()


# Query para obetener cupones que tienen descuento
def getCouponWithDiscount(self, engine):
    with engine.connect() as connection:
        result = connection.execute(
            text(
                "SELECT id_coupon, coupon_code FROM coupons WHERE discount IS NOT NULL;"
            )
        )
    return result.fetchone()


# Query para obetener cupones que NO tienen descuento
def getCouponWithoutDiscount(self, engine):
    with engine.connect() as connection:
        result = connection.execute(
            text("SELECT id_coupon, coupon_code FROM coupons WHERE discount IS NULL;")
        )
    return result.fetchone()
