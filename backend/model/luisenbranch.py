from flask import Flask, request, jsonify

app = Flask(__name__)

# Datos quemados para productos
productos = [
    {"id": 1, "nombre": "Producto 1", "descripcion": "Descripción del producto 1"},
    {"id": 2, "nombre": "Producto 2", "descripcion": "Descripción del producto 2"},
]

# Método para obtener todos los productos
@app.route('/productos', methods=['GET'])
def get_productos():
    return jsonify(productos)

# Método para agregar un nuevo producto
@app.route('/productos', methods=['POST'])
def add_producto():
    data = request.get_json()
    nombre = data['nombre']
    descripcion = data['descripcion']

    # Generar un nuevo ID basado en el último ID existente
    new_id = productos[-1]['id'] + 1 if productos else 1

    nuevo_producto = {"id": new_id, "nombre": nombre, "descripcion": descripcion}
    productos.append(nuevo_producto)

    return jsonify({'message': 'Producto agregado exitosamente!'})

if __name__ == '__main__':
    app.run(debug=True)
