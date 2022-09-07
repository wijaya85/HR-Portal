from django.urls import path
from .views import test, home

urlpatterns = [
    path('', test),
    path('home', home)
]