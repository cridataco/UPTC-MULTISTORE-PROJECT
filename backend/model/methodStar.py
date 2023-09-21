class DatabaseFalse:
    def __init__(self):
        #datos quemados simulando la base de datos
        self.productos = [
            {"id": 1, "nombre": "Producto A", "estrellas": 4},
            {"id": 2, "nombre": "Producto B", "estrellas": 3},
            {"id": 3, "nombre": "Producto C", "estrellas": 5},
        ]

    def obtener_estrellas_producto(self, producto_id):

        for producto in self.productos:
            if producto["id"] == producto_id:
                return producto["estrellas"]
        return None

    def actualizar_estrellas_producto(self, producto_id, nuevas_estrellas):

        for producto in self.productos:
            if producto["id"] == producto_id:
                producto["estrellas"] = nuevas_estrellas
                return True
        return False

    def calcular_promedio_estrellas(self):

        total_estrellas = sum(producto["estrellas"] for producto in self.productos)
        cantidad_productos = len(self.productos)
        if cantidad_productos > 0:
            return total_estrellas / cantidad_productos
        else:
            return 0.0



