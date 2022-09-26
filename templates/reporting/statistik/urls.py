"""hrportal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from home.views import index
from base_auth.views import login, reset_password
from about_us.views import visi_misi, struktur_organisasi
from layanan_prima.views import data_statistik, pencarian_pegawai
from galery_sdm.views import video, infografik
from faq.views import faq
from user_profile.views import profile, data_pribadi 
from agenda.views import agenda
from beasiswa.views import beasiswa
from pegawai_pensiun.views import pegawai_pensiun
from pengumuman.views import pengumuman
from manajemen_pns.views import peraturan_kepegawaian, kartu_pegawai, cuti_pegawai, kenaikan_pangkat, kode_etik, pengangkatan_cpns, gaji_cpns, manajemen_talenta
from hrportal_api.views import loginCallback, tokenCallback
from django.conf import settings
from django.conf.urls.static import static

#API PART
# from rest_framework import routers
# from hrportal_api.views import *

# router = routers.DefaultRouter()
# router.register('5-pengumuman-terbaru', PengumumanTerbaruView)
# router.register('sebaran=')
# router.register('video', VideoView)
# router.register('infografis', InfografisView)
# router.register('peraturan', PeraturanView)
# router.register('pengumuman', PengumumanView)

urlpatterns = [
    path('api/', include('hrportal_api.urls')),
    path('login-callback/', loginCallback, name='login_callback'),
    path('token-callback/', tokenCallback, name='token_callback'),
    path('manajemen_pns/', include('manajemen_pns.urls', namespace='manajemen_pns')),
    path('layanan_prima/', include('layanan_prima.urls', namespace='layanan_prima')),
    path('galery_sdm/', include('galery_sdm.urls', namespace='galery_sdm')),
    path('about_us/', include('about_us.urls', namespace='about_us')),
    path('faq/', include('faq.urls', namespace='faq')),
    path('profile/', include('user_profile.urls', namespace='user_profile')),
    path('agenda/', include('agenda.urls', namespace='agenda')),
    path('beasiswa/', include('beasiswa.urls', namespace='beasiswa')),
    path('pegawai_pensiun/', include('pegawai_pensiun.urls', namespace='pegawai_pensiun')),
    path('pengumuman/', include('pengumuman.urls', namespace='pengumuman')),
    path('eom/', include('eom.urls', namespace='eom')),
    path('pegawai_teladan/', include('pegawai_teladan.urls', namespace='pegawai_teladan')),
    path('admin/', admin.site.urls),
    path('login/', login, name='login'),
    path('resetpassword/', reset_password, name='resetpassword'),
    path('', index, name='index'),
    path('auth/', include('rest_framework.urls', namespace='rest_framework'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)