from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('detail/<int:barangid>', views.detail, name='detail'),
    path('detail/tambah/', views.input_barang, name='tambah'),
]