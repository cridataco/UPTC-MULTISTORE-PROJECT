from sqlalchemy import text
from sqlalchemy.orm.session import Session
from models.user import User


# Query Create User
def createUser(session: Session, user: User):
    session.add(user)
    session.commit()


# Query Select User by id_user
def getUserByIdUser(session: Session, id_user):
    return session.query(User).filter_by(id_user=id_user).first()


# Query Select Users by username
def getUsersByUserName(session: Session, username):
    return session.query(User).filter_by(username=username).all()


# Query Select User by email
def getUserByEmail(session: Session, email):
    return session.query(User).filter_by(email=email).first()


# Query Client Users (is_client == 2)
def getClientUsers(session: Session):
    return session.query(User).filter_by(is_client=2).all()


# Query Select Users by date_account_creation
def getUsersByCreationDate(session: Session, date):
    return session.query(User).filter_by(date_account_creation=date).all()


# Query Get id_platform by id_user
def getIdPlatform(session: Session, id_user):
    return session.query(User.id_platform).filter_by(id_user=id_user).scalar()


# Query Get email by id_user
def getEmail(session: Session, id_user):
    return session.query(User.email).filter_by(id_user=id_user).scalar()


# Query Get user_name by id_user
def getUserName(session: Session, id_user):
    return session.query(User.user_name).filter_by(id_user=id_user).scalar()


# Query Get birthdate by id_user
def getBirthdate(session: Session, id_user):
    return session.query(User.birthdate).filter_by(id_user=id_user).scalar()


# Query Get document_number by id_user
def getDocumentNumber(session: Session, id_user):
    return session.query(User.document_number).filter_by(id_user=id_user).scalar()


# Query Get document_type by id_user
def getDocumentType(session: Session, id_user):
    return session.query(User.document_type).filter_by(id_user=id_user).scalar()


# Query Get is_client by id_user
def getIsClient(session: Session, id_user):
    return session.query(User.is_client).filter_by(id_user=id_user).scalar()


# Query Get cell_phone_number by id_user
def getCellPhoneNumber(session: Session, id_user):
    return session.query(User.cell_phone_number).filter_by(id_user=id_user).scalar()


# Query Get user_rol id_user
def getUserRol(session: Session, id_user):
    return session.query(User.user_rol).filter_by(id_user=id_user).scalar()


# Query Get user_permissions by id_user
def getUserPermissions(session: Session, id_user):
    return session.query(User.user_permissions).filter_by(id_user=id_user).scalar()


# Query Get date_account_creation by id_user
def getDateAccountCreation(session: Session, id_user):
    return session.query(User.date_account_creation).filter_by(id_user=id_user).scalar()


# Query Delete User
def deleteUser(session: Session, id_user):
    user_to_delete = getUserByIdUser(session=session, id_user=id_user)
    if user_to_delete:
        session.delete(user_to_delete)
        session.commit()
        return True
    else:
        return False


# Query Update id_platform
def updateIdPlatform(session: Session, id_user, id_platform):
    user_to_update = getUserByIdUser(session=session, id_user=id_user)
    if user_to_update:
        user_to_update.id_platform = id_platform
        session.commit()
        return True
    else:
        return False


# Query Update email
def updateEmail(session: Session, id_user, email):
    user_to_update = getUserByIdUser(session=session, id_user=id_user)
    if user_to_update:
        user_to_update.email = email
        session.commit()
        return True
    else:
        return False


# Query Update user_name
def updateUserName(session: Session, id_user, user_name):
    user_to_update = getUserByIdUser(session=session, id_user=id_user)
    if user_to_update:
        user_to_update.user_name = user_name
        session.commit()
        return True
    else:
        return False


# Query Update birthdate
def updateBirthdate(session: Session, id_user, birthdate):
    user_to_update = getUserByIdUser(session=session, id_user=id_user)
    if user_to_update:
        user_to_update.birthdate = birthdate
        session.commit()
        return True
    else:
        return False


# Query Update document_number
def updateDocumentNumber(session: Session, id_user, document_number):
    user_to_update = getUserByIdUser(session=session, id_user=id_user)
    if user_to_update:
        user_to_update.document_number = document_number
        session.commit()
        return True
    else:
        return False


# Query Update document_type
def updateDocumentType(session: Session, id_user, document_type):
    user_to_update = getUserByIdUser(session=session, id_user=id_user)
    if user_to_update:
        user_to_update.document_type = document_type
        session.commit()
        return True
    else:
        return False


# Query Update is_client
def updateIsClient(session: Session, id_user, is_client):
    user_to_update = getUserByIdUser(session=session, id_user=id_user)
    if user_to_update:
        user_to_update.is_client = is_client
        session.commit()
        return True
    else:
        return False


# Query Update cell_phone_number
def updateCellPhoneNumber(session: Session, id_user, cell_phone_number):
    user_to_update = getUserByIdUser(session=session, id_user=id_user)
    if user_to_update:
        user_to_update.cell_phone_number = cell_phone_number
        session.commit()
        return True
    else:
        return False


# Query Update user_rol
def updateUserRol(session: Session, id_user, user_rol):
    user_to_update = getUserByIdUser(session=session, id_user=id_user)
    if user_to_update:
        user_to_update.user_rol = user_rol
        session.commit()
        return True
    else:
        return False


# Query Update user_permissions
def updateUserPermissions(session: Session, id_user, user_permissions):
    user_to_update = getUserByIdUser(session=session, id_user=id_user)
    if user_to_update:
        user_to_update.user_permissions = user_permissions
        session.commit()
        return True
    else:
        return False


# Query Set date_account_deletion
def setDateAccountDeletion(session: Session, id_user, date_account_deletion):
    user_to_update = getUserByIdUser(session=session, id_user=id_user)
    if user_to_update:
        user_to_update.date_account_deletion = date_account_deletion
        session.commit()
        return True
    else:
        return False


# Query Count Users
def getTotalUsers(session: Session):
    return session.query(User.id_user).count()


# Query Select Older user created
def getOlderUserCreated(session: Session):
    query = text(
        """SELECT * FROM users 
            ORDER BY date_account_creation 
            ASC LIMIT 1;"""
    )
    result = session.execute(query)
    return rowToUser(result.fetchone())


# Query Select NewestUser
def getNewestUser(session: Session):
    query = text(
        """SELECT * FROM users 
            ORDER BY date_account_creation 
            DESC LIMIT 1;"""
    )
    result = session.execute(query)
    return rowToUser(result.fetchone())


# Query Select the user with the most products purchased
def getTheMostProductsPurchased(session: Session):
    query = text(
        """SELECT id_user, user_name, 
            COUNT (product.id_product) AS quantity_products 
            FROM users INNER JOIN orders ON users.id_user = orders.id_user 
            INNER JOIN order_details ON orders.id_order = order_details.id_order 
            INNER JOIN product_stock ON order_details.SKU = product_stock.SKU 
            INNER JOIN product ON order_details.id_product = product.id_product 
            GROUP BY id_user, user_name 
            ORDER BY quantity_products DESC LIMIT 1;"""
    )
    query2 = text(
        """SELECT id_user, user_name
            FROM users u, orders o, order_details od
            WHERE u.id_user = o.id_user 
            AND od.id_order = o.id_order
            AND od.id_order = (SELECT ID_ORDER FROM ORDER_DETAILS
            WHERE QUANTITY = (SELECT MAX(QUANTITY) FROM ORDER_DETAILS));"""
    )
    # Falta probarlas
    result = session.execute(query)
    return rowToUser(result.fetchone())


# Query Select the user with the fewest products purchased
def getTheFewestProductsPurchased(session: Session):
    query = text(
        """SELECT id_user, user_name, 
            COUNT (product.id_product) AS quantity_products 
            FROM users INNER JOIN orders ON users.id_user = orders.id_user 
            INNER JOIN order_details ON orders.id_order = order_details.id_order 
            INNER JOIN product_stock ON order_details.SKU = product_stock.SKU 
            INNER JOIN product ON order_details.id_product = product.id_product 
            GROUP BY id_user, user_name 
            ORDER BY quantity_products ASC LIMIT 1;"""
    )
    # Falta probarla
    result = session.execute(query)
    return rowToUser(result.fetchone())


# Map Row To User Object
def rowToUser(row):
    if row:
        return User(
            id_user=row[0],
            id_platform=row[1],
            email=row[2],
            user_name=row[3],
            birthdate=row[4],
            document_number=row[5],
            document_type=row[6],
            is_client=row[7],
            cell_phone_number=row[8],
            user_rol=row[9],
            user_permissions=row[10],
            date_account_creation=row[11],
            date_account_deletion=row[12] if row[12] else None,
        )
    else:
        return None


# Map Sequense to User List
def sequenseToUsers(sequense) -> list[User]:
    if sequense:
        users = []
        for row in sequense:
            user = rowToUser(row)
            users.append(user)
        return users
    else:
        return None
