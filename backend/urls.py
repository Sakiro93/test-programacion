from django.urls import path

from backend.view_product import productListView
from backend.views import *

urlpatterns = [
    #Funciones con Serialize
    path('product/', list_products, name='list_products'),
    path('product/add/', create_product, name='create_product'),
    path('product/update/<int:id>/', update_product, name='update_product'),
    path('product/delete/<int:id>/', delete_product, name='delete_product'),

    path('category/', list_categories, name='list_categories'),
    path('category/add/', create_category, name='create_category'),
    path('category/update/<int:id>/', update_product, name='update_category'),
    path('category/delete/<int:id>/', delete_category, name='delete_category'),

    path('categoryclient/', list_categoriesclient, name='list_categoriesclient'),
    path('categoryclient/add/', create_categoryclient, name='create_categoryclient'),
    path('categoryclient/update/<int:id>/', update_categoryclient, name='update_categoryclient'),
    path('categoryclient/delete/<int:id>/', delete_categoryclient, name='delete_categoryclient'),

    #Vista con ListApiView
    path('productview/', productListView.as_view(), name='product_list_view'),
    path('productview/<int:id>/', productListView.as_view(), name='product_list_view_with_id'),

]