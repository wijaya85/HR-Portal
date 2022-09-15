from django.urls import path
from .views import infografisList, addInfografis, editInfografis

app_name = 'galeri_sdm'

urlpatterns = [
    path('infografis/', infografisList, name='daftar_infografis'),
    path('infografis/add', addInfografis, name='add_infografis'),
    path('infografis/edit/<int:id>', editInfografis, name='edit_infografis'),
]