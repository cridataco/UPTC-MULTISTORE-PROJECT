from django.urls import path
from .views import ProductAPI

urlpatterns = [
    path('productos', ProductAPI.receive_and_create_product),
    path('productos/<int:prod_id>', ProductAPI.get_product),
    path('actualizar-producto/<int:prod_id>', ProductAPI.update_product),
    path('eliminar-producto/<int:prod_id>', ProductAPI.delete_product),
]