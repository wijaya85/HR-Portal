from django.urls import path
from .views import deleteInfografis, editVideo, infografisList, addInfografis, editInfografis, listBanner, addBanner, detailBanner, editBanner, deleteBanner, listVideo, addVideo, deleteVideo, detailInfografis, detailVideo

app_name = 'galeri_sdm'

urlpatterns = [
    path('infografis/', infografisList, name='daftar_infografis'),
    path('infografis/add', addInfografis, name='add_infografis'),
    path('infografis/edit/<int:id>', editInfografis, name='edit_infografis'),
    path('infografis/delete/<int:id>', deleteInfografis, name='delete_infografis'),
    path('infografis/detail/<int:id>', detailInfografis, name='detail_infografis'),
    path('banner/', listBanner, name='daftar_banner'),
    path('banner/add', addBanner, name='add_banner'),
    path('banner/detail/<int:id>', detailBanner, name='detail_banner'),
    path('banner/edit/<int:id>', editBanner, name='edit_banner'),
    path('banner/delete/<int:id>', deleteBanner, name='delete_banner'),
    path('video/', listVideo, name='daftar_video'),
    path('video/add', addVideo, name='add_video'),
    path('video/edit/<int:id>', editVideo, name='edit_video'),
    path('video/delete/<int:id>', deleteVideo, name='delete_video'),
    path('video/detail/<int:id>', detailVideo, name='detail_video'),
]