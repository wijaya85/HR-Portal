from django.urls import path
from .views import list, add, edit, detail

app_name = 'pengumuman'

urlpatterns = [
    path('', list, name='daftar_pengumuman'),
    path('add', add, name='add_pengumuman'),
    path('edit/<int:id>', edit, name='edit_pengumuman'),
    path('detail/<int:id>', detail, name='detail_pengumuman'),
]