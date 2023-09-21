# Base de datos con datos quemados.
base_de_datos = {
    1: {'nombre': 'Producto 1', 'comentarios': {}},
    2: {'nombre': 'Producto 2', 'comentarios': {}},
    3: {'nombre': 'Producto 3', 'comentarios': {}},
    4: {'nombre': 'Producto 4', 'comentarios': {}},
}


# Método para agregar o editar un comentario
def agregar_editar_comentario(producto_id, usuario, contenido):
    if producto_id not in base_de_datos:
        return "Producto no encontrado"

    if contenido == "":
        return "El comentario no puede estar vacío"

    # Verificar si el usuario ya ha comentado en este producto
    if usuario in base_de_datos[producto_id]['comentarios']:
        # El usuario ya ha comentado, por lo que este será un intento de edición
        base_de_datos[producto_id]['comentarios'][usuario] = contenido
        return "Comentario editado correctamente"
    else:
        # El usuario no ha comentado, este será un nuevo comentario
        base_de_datos[producto_id]['comentarios'][usuario] = contenido
        return "Comentario agregado correctamente"


# Método para obtener el comentario de un usuario en un producto
def obtener_comentario(producto_id, usuario):
    if producto_id not in base_de_datos:
        return "Producto no encontrado"

    if usuario in base_de_datos[producto_id]['comentarios']:
        return base_de_datos[producto_id]['comentarios'][usuario]
    else:
        return f"El usuario {usuario} no ha comentado en este producto"


# Método para enviar comentarios a la Base de Datos, en caso que esta ya este vinculada.
def enviar_comentarios_a_base_de_datos():
    # Aquí se realizaría el envío a la base de datos.
    pass


# Método para recuperar comentarios de la Base de Datos, en caso que esta ya este vinculada.
def recuperar_comentarios_de_base_de_datos():
    # Aquí se realizaría la recuperación desde la base de datos.
    pass
