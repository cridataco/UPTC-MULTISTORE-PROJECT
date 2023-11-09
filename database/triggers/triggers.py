from sqlalchemy import create_engine, text, event
from sqlalchemy.orm import sessionmaker

# Configura tu conexión a la base de datos con SQLAlchemy
DB_URI = "mysql+mysqlconnector://usuario:contraseña@localhost/nombre_basedatos"
engine = create_engine(DB_URI)

# Crear el procedimiento almacenado con SQLAlchemy
create_procedure_query = """
CREATE PROCEDURE GenerateDispatchReport()
BEGIN
    SELECT *
    FROM orders
    WHERE state = 'Pending'
    AND DATE(delivery_date) = CURDATE(); 
END;
"""

# Ejecuta el comando SQL
with engine.connect() as connection:
    connection.execute(text(create_procedure_query))

# Crear el evento (trigger) con SQLAlchemy
create_event_query = """
CREATE EVENT IF NOT EXISTS DailyDispatchReport
ON SCHEDULE EVERY 1 DAY
DO
BEGIN
    CALL GenerateDispatchReport();
END;
"""

# Ejecuta el comando SQL
with engine.connect() as connection:
    connection.execute(text(create_event_query))

# TRIGGER PARA prevenir eliminar un usuario si no es administrador con SQLAlchemy
trigger_prevent_delete_admin = """
CREATE TRIGGER prevent_delete_admin
BEFORE DELETE ON users
FOR EACH ROW
BEGIN
    IF OLD.is_client = 2 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'No se puede eliminar un administrador';
    END IF;
END;
"""

# Ejecuta el comando SQL
with engine.connect() as connection:
    connection.execute(text(trigger_prevent_delete_admin))

# TRIGGER PARA prevenir agregar usuario fuera del horario permitido con SQLAlchemy
trigger_add_user_in_specific_time = """
CREATE TRIGGER insert_user_in_specifi_time
BEFORE INSERT ON users
FOR EACH ROW
BEGIN
    DECLARE hora_actual TIME;
    SET hora_actual = CURRENT_TIME();

    IF hora_actual <= '08:00:00' AND hora_actual >= '20:00:00' THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'No se pueden agregar usuarios fuera del horario permitido (8 a.m. - 8 p.m)';
    END IF;
END;
"""

# Ejecuta el comando SQL
with engine.connect() as connection:
    connection.execute(text(trigger_add_user_in_specific_time))

# TRIGGER PARA notificar bajo stock con SQLAlchemy
trigger_low_stock_notification = """
CREATE TRIGGER low_stock_notification
AFTER UPDATE ON product_stock
FOR EACH ROW
BEGIN
    IF NEW.current_stock < 10 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Bajo stock para el producto X';
    END IF;
END;
"""

# Ejecuta el comando SQL
with engine.connect() as connection:
    connection.execute(text(trigger_low_stock_notification))

# Utilizando eventos SQLAlchemy para simular TRIGGERS
@event.listens_for(engine, "before_cursor_execute")
def before_cursor_execute(conn, cursor, statement, parameters, context, executemany):
    if "prevent_delete_admin" in statement:
        raise Exception("No se puede eliminar un administrador")

# Puedes agregar más eventos según sea necesario para otros TRIGGERS

# Ahora puedes utilizar SQLAlchemy normalmente para interactuar con la base de datos
Session = sessionmaker(bind=engine)
session = Session()