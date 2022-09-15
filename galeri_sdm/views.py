from pyexpat import model
from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from .models import Infografis
from .forms import InfografisForm

# Create your views here.
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