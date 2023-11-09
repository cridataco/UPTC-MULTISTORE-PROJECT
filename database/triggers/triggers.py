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
