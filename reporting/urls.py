from django.urls import path
from .views import  StatistikGender, StatistikPendidikan, StatistikGolongan, test, petaSebaranPegawai

app_name = 'reporting'

urlpatterns = [
    path('', test),
    path('gender', StatistikGender),
    path('golongan', StatistikGolongan),
    path('pendidikan', StatistikPendidikan),
    path('peta', petaSebaranPegawai)
]