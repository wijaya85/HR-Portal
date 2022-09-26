from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from .models import Infografis, Banner, Video
from .forms import InfografisForm, BannerForm, VideoForm

# Infografis
def infografisList(request):
    template_name = 'galery_sdm/infografis/list.html'
    judul = "Daftar Infografis"
    model = Infografis
    data = model.objects.all().order_by()
    context = ({'data': data, 'judul': judul})
    return render(request, template_name, context)


def addInfografis(request):
    template_name = 'galery_sdm/infografis/create.html'
    form = InfografisForm(request.POST or None)
    if request.method == 'POST':
        form = InfografisForm(request.POST, request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect(reverse('galeri_sdm:daftar_infografis'))
    context = ({'form': form})
    return render(request, template_name, context)


def editInfografis(request, id):
    template_name = 'galery_sdm/infografis/edit.html'
    obj = Infografis.objects.get(id=id)
    context = {}
    #object = get_object_or_404(KategoriPengumuman, id=id)
    if request.method == 'POST':
        form = InfografisForm(request.POST, request.FILES, instance=obj)
        if form.is_valid():
            form.save()
            return redirect(reverse('galeri_sdm:daftar_infografis'))
    else:
        form = InfografisForm(instance=obj)
        context['form'] = form
    return render(request, template_name, context)


def deleteInfografis(request,id):
    contex = {}
    obj = Infografis.objects.get(id=id)
    if id:
        obj.delete()
    return redirect(reverse('galeri_sdm:daftar_infografis'))


def detailInfografis(request, id):
    template_name = 'galery_sdm/infografis/detail.html'
    query = Infografis.objects.get(id=id)
    context = {'object': query}
    if query:
        return render(request, template_name, context)
    else:
        return redirect(reverse('galeri_sdm:daftar_infografis'))

# Banner
def listBanner(request):
    template_name = 'galery_sdm/banner/list.html'
    judul = "Daftar Banner"
    model = Banner
    data = model.objects.all().order_by()
    context = ({'data': data, 'judul': judul})
    return render(request, template_name, context)


def addBanner(request):
    template_name = 'galery_sdm/banner/create.html'
    form = BannerForm(request.POST or None)
    if request.method == 'POST':
        form = BannerForm(request.POST, request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect(reverse('galeri_sdm:daftar_banner'))
    context = ({'form': form})
    return render(request, template_name, context)


def editBanner(request, id):
    template_name = 'galery_sdm/banner/edit.html'
    object = Banner.objects.get(id=id)
    context = {}
    if request.method == 'POST':
        form = BannerForm(request.POST, request.FILES, instance=object)
        if form.is_valid():
            form.save()
            return redirect(reverse('galeri_sdm:daftar_banner'))
    else:
        form = BannerForm(instance=object)
        context['form'] = form
    context = ({'form': form})
    return render(request, template_name, context)


def detailBanner(request, id):
    template_name = 'galery_sdm/banner/detail.html'
    query = Banner.objects.get(id=id)
    context = {'object': query}
    if query:
        return render(request, template_name, context)
    else:
        return redirect(reverse('galeri_sdm:daftar_banner'))


def deleteBanner(request, id):
    contex = {}
    object = Banner.objects.get(id=id)
    if id:
        object.delete()
    return redirect(reverse('galeri_sdm:daftar_banner'))
    
# Video
def listVideo(request):
    template_name = 'galery_sdm/video/list.html'
    judul = "Daftar Video"
    model = Video
    data = model.objects.all().order_by()
    context = ({'data': data, 'judul': judul})
    return render(request, template_name, context)


def addVideo(request):
    template_name = 'galery_sdm/video/create.html'
    form = VideoForm(request.POST or None)
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect(reverse('galeri_sdm:daftar_video'))
    context = ({'form': form})
    return render(request, template_name, context)


def editVideo(request, id):
    template_name = 'galery_sdm/video/edit.html'
    object = Video.objects.get(id=id)
    context = {}
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect(reverse('galeri_sdm:daftar_video'))
    else:
        form = VideoForm(instance=object)
        context['form'] = form
    context = ({'form': form})
    return render(request, template_name, context)


def deleteVideo(request,id):
    template_name = 'pengumuman/delete_view.html'
    obj = Video.objects.get(id=id)
    if id:
        obj.delete()
    return redirect(reverse('galeri_sdm:daftar_video'))


def detailVideo(request, id):
    template_name = 'galery_sdm/video/detail.html'
    object = Video.objects.get(id=id)
    context = {'object': object}
    if object:
        return render(request, template_name, context)
    else:
        return redirect(reverse('galeri_sdm:daftar_video'))