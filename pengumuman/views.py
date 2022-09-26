from re import template
from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from .forms import PengumumanForm
from .models import Pengumuman

# Create your views here.
def list(request):
    template_name = 'pengumuman/list.html'
    judul = 'Daftar Pengumuman'
    search = request.GET.get('cari_pengumuman')
    if search:
        data = Pengumuman.objects.filter(judul__icontains=search)
    else:
        data = Pengumuman.objects.all().order_by('-id')
    context = ({'judul': judul, 'data': data})
    return render(request, template_name, context)

def add(request):
    template_name = 'pengumuman/create.html'
    form = PengumumanForm(request.POST or None)
    if request.method == 'POST':
        form = PengumumanForm(request.POST, request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect(reverse('pengumuman:daftar_pengumuman'))
    context = ({'form': form})
    return render(request, template_name, context)

def edit(request, id):
    template_name = 'pengumuman/edit.html'
    obj = Pengumuman.objects.get(id=id)
    context = {}
    #object = get_object_or_404(KategoriPengumuman, id=id)
    if request.method == 'POST':
        form = PengumumanForm(request.POST, request.FILES, instance=obj)
        if form.is_valid():
            form.save()
            return redirect(reverse('pengumuman:daftar_pengumuman'))
    else:
        form = PengumumanForm(instance=obj)
        context['form'] = form
    return render(request, template_name, context)

def detail(request, id):
    template_name = 'pengumuman/detail.html'
    obj = Pengumuman.objects.get(id=id)
    context = {'object': obj}
    if obj:
        return render(request, template_name, context)
    else:
        return redirect(reverse('pengumuman:daftar_pengumuman'))
    
def delete(request,id):
    template_name = 'pengumuman/delete_view.html'
    obj = Pengumuman.objects.get(id=id)
    if id:
        obj.delete()
    return redirect(reverse('pengumuman:daftar_pengumuman'))