from django.urls import path
from. views import product_info_json, product_info_pdf, buy_product

urlpatterns = [
    path('product_json', product_info_json),
    path('product_pdf', product_info_pdf),
    path('<int:quantity>', buy_product),
]