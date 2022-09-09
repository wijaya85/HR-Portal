from django.urls import path
from .views import test, StatistikGender, StatistikPendidikan, StatistikGolongan

app_name = 'reporting'

urlpatterns = [
    path('', test),
    path('gender', StatistikGender),
    path('golongan', StatistikGolongan),
    path('pendidikan', StatistikPendidikan)
]