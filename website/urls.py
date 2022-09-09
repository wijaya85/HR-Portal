from tkinter import N
from django.urls import path
from .views import test, home, login_view

app_name = 'website'

urlpatterns = [
    path('', test),
    path('home', home),
    path('login', login_view, name='login_view'),
]