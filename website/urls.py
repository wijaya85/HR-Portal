from tkinter import N
from django.urls import path
from .views import test, home, login_view, pencarian, infografis

app_name = 'website'

urlpatterns = [
    path('', test),
    path('home', home),
    path('login', login_view, name='login_view'),
    path('pencarian', pencarian, name='pencarian'),
    path('infografis', infografis, name='infografis'),
]