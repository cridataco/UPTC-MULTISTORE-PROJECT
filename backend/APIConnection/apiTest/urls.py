from django.urls import path
from .views import ProductAPI

urlpatterns = [
    path('product', ProductAPI.receive_and_create_product),
    path('product/<int:prod_id>', ProductAPI.get_product),
    path('update-product/<int:prod_id>', ProductAPI.update_product),
    path('delete-product/<int:prod_id>', ProductAPI.delete_product),
]
