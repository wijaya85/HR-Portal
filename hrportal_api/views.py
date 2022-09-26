from pengumuman.models import Pengumuman
from rest_framework import viewsets
from .serializers import PengumumanSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import render
from pegawai.models import DataLengkap
from django.db import connection


def dictfetchall(cursor):
  "Return all rows from a cursor as a dict"
  columns = [col[0] for col in cursor.description]
  return [
      dict(zip(columns, row))
      for row in cursor.fetchall()
  ]

class PengumumanViewSet(viewsets.ModelViewSet):
    queryset = Pengumuman.objects.all()
    serializer_class = PengumumanSerializer

@api_view(['GET'])
def findPegawaiByRegional(request):
  cursor = connection.cursor()
  cursor.execute('''select ProvinsiKantor, count(*) jumlah from dev_websdm.dbo.data_lengkap group by ProvinsiKantor order by ProvinsiKantor''')
  data = dictfetchall(cursor)
  return Response(data)
    

@api_view(['GET'])    
def loginCallback(request):
    request_code = request.GET["code"]
    
    data = {
        'grant_type': 'authorization_code',
        'code': request_code,
        'redirect_uri': 'http://localhost:8000/api/login-callback',
        'client_id': 'portal-sdm',
        'scope': 'openid profile profil.hris'
    }
    
    headers = {
        'Content-Type': "application/x-www-form-urlencoded",
        'Accept': "*/*",
    }
    
    r = requests.post(url = 'https://demo-account.kemenkeu.go.id/connect/token', data = data, headers= headers)
    
    response_api = r.json()
    userInfoHeaders = {
        'Authorization': 'Bearer ' + response_api['access_token']
    }
    
    user_info = requests.get(url = 'https://demo-account.kemenkeu.go.id/connect/userinfo', headers=userInfoHeaders)
    
    response_user_info = user_info.json()
    
    output = {
        'user_name': response_user_info['name'],
        'user_email': response_user_info['email'],
        'token': response_api['access_token']
    }
    
    request.COOKIES['access_token'] = response_api['access_token']
    request.COOKIES['name'] = response_user_info['name']
    responseData = render(request, 'loading/index.html')
    
    responseData.set_cookie(key='access_token', value=response_api['access_token'])
    responseData.set_cookie(key='name', value=response_user_info['name'])
    print(response_user_info, '<<<<<<<<<<<<<<<<<< response user info')
    return responseData


@api_view(['GET'])
def tokenCallback(request):
  print(request.GET, '<<<<<<<<<<<<<<<<< this is get')
  
  return render(request, 'loading/token.html')

