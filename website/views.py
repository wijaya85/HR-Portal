from re import search
from django.shortcuts import render, reverse, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from galeri_sdm.models import Banner, Infografis, Video
from pengumuman.models import Pengumuman
# Create your views here.

def test(request):
    return HttpResponse("website")

def home(request):
    banner = Banner.objects.filter(publish=True)
    video = Video.objects.filter(publish=True)
    pengumuman = Pengumuman.objects.filter(publish=True).order_by('-tanggalCreate')[:5]
    context = ({'banner':banner, 'video':video, 'pengumuman':pengumuman})
    return render(request, 'home/index.html', context)

def login_view(request):
    template_name = 'login/login.html'
    form = LoginForm(request.POST or None)
    
    if request.user.is_authenticated:
        next_url = request.GET.get('next')
        if next_url:
            return HttpResponseRedirect(next_url)
        return redirect(reverse('web:admin-index'))
    
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')  #menghindari karakter2 berbahaya
            password = form.cleaned_data.get('password')
           
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                
                return redirect(reverse('web:admin-index'))
        
    return render(request,template_name,{'form':form})


def pencarian(request):
    serach = request.GET.get('pencarian')
    contex = {}
    if search:
        query = DataLengkap.objects.filter(namalengkap__icontains=search)
    
    return render(request, 'home/pencarian.html')

def infografis(request):
    data = Infografis.objects.all()
    context = ({'data':data})
    return render(request, 'home/galeri/infografis.html', context)