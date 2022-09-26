from django.urls import path, include
from rest_framework import routers
from .views import PengumumanViewSet, loginCallback, findPegawaiByRegional

router = routers.DefaultRouter()
router.register(r'pengumuman_api', PengumumanViewSet)
#router.register(r'loginCallback', loginCallback)

urlpatterns = [
    path('', include(router.urls)),
    path('pegawai-by-regional', findPegawaiByRegional),
    #path('api-auth/', include('rest_frameworks.urls', namespace='rest_framework')),
]
