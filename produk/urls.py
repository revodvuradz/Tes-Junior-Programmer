from django.urls import path
from . import views

urlpatterns = [
    path('', views.produk_list, name='produk_list'),
    path('tambah/', views.produk_create, name='produk_create'),
    path('edit/<int:pk>/', views.produk_update, name='produk_update'),
    path('bulk-delete/', views.produk_bulk_delete, name='produk_bulk_delete'),

]
