from django.urls import path
from .views import test, StatistikGender

app_name = 'reporting'

urlpatterns = [
    path('', test),
    path('gender', StatistikGender),
]