import sqlite3
import flet as ft, jsonify
from flet_core import FletApp

app = FletApp(__name__)

def obtener_videos_y_fotos(producto_id):
    conn = sqlite3.connect('mi_base_de_datos.db')
    cursor = conn.cursor()

    cursor.execute("SELECT video_url, foto_url FROM productos WHERE id=?", (producto_id,))
    data = cursor.fetchone()

    conn.close()

    if not data:
        return {}

    videos_fotos = {
        'video_url': data[0],
        'foto_url': data[1]
    }
    return videos_fotos

@app.route('/producto/<int:producto_id>/videos-fotos', methods =['GET'])
def obtener_videos_fotos_producto(producto_id):
    videos_fotos = obtener_videos_y_fotos(producto_id)
    return jsonify(videos_fotos)



