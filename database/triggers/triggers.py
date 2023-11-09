
import mysql.connector

# Conectar a la base de datos
conn = mysql.connector.connect( #coneccion a la base de datos
    host="tu_host",
    user="tu_usuario", 
    password="tu_contraseña",
    database="tu_base_de_datos"
)

# Crear un cursor
cursor = conn.cursor()

# Crear el procedimiento almacenado
create_procedure_query = """
DELIMITER //

CREATE PROCEDURE GenerateDispatchReport()
BEGIN
    SELECT *
    FROM orders
    WHERE state = 'Pending' -- no enviado aun
    AND DATE(delivery_date) = CURDATE(); 
END //

DELIMITER ;
"""
#la funcion CURDATE() devuelve la fecha actual del en el formato 'YYYY-MM-DD'. tambien se puede usar SYSdate.

cursor.execute(create_procedure_query)

# Crear el evento (trigger)
create_pedidos_query = """
CREATE EVENT IF NOT EXISTS DailyDispatchReport
ON SCHEDULE EVERY 1 DAY
DO
BEGIN
    CALL GenerateDispatchReport();
END;
"""

cursor.execute(create_pedidos_query)

# Confirmar los cambios y cerrar la conexión
conn.commit()
conn.close()

from sqlalchemy import text
from sqlalchemy import create_engine

# Configura tu conexión a la base de datos
DB_URI = "mysql+mysqlconnector://usuario:contraseña@localhost/nombre_basedatos"
engine = create_engine(DB_URI)

# TRIGGER PARA prevenir eliminar un usuario si no es administrador
trigger_prevent_delete_admin = """
CREATE TRIGGER prevent_delete_admin
BEFORE DELETE ON users
FOR EACH ROW
BEGIN
    IF users.is_client = 2 THEN SIGNAL SQLSTATE '45000' 
    SET MESSAGE_TEXT = 'No se puede eliminar un administrador';
    END IF;
END;  
"""
# Ejecuta el comando SQL
with engine.connect() as connection:
    connection.execute(text(trigger_prevent_delete_admin))

# TRIGGER PARA prevenir eliminar un usuario si no es administrador
trigger_add_user_in_specific_time = """
CREATE TRIGGER insert_user_in_specifi_time
BEFORE INSERT ON users
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

