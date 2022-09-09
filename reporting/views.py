from django.shortcuts import render
from django.http import HttpResponse
from .models import TempDataLengkap092022
from django.db.models import Count, Case, When, IntegerField
import json

# Create your views here.
def test(request):
    labelsUnit = []
    dataUnit = []
    labelsGender = []
    dataGender = []
    model = TempDataLengkap092022
    perUnit = model.objects.all().values('unitsingkat').annotate(
        jumlah=Count('idpegawai'),
    ).order_by('unitsingkat')
    for a in perUnit:
        labelsUnit.append(a['unitsingkat'])
        dataUnit.append(a['jumlah'])
        
    gender = model.objects.all().values('kodekelamin').annotate(
        jumlah=Count('idpegawai'),
    ).order_by('kodekelamin')
    
    for b in gender:
        labelsGender.append(b['kodekelamin'])
        dataGender.append(b['jumlah'])
    
    context = ({'labelsUnit': json.dumps(labelsUnit), 
                'dataUnit': json.dumps(dataUnit),
                'labelsGender':json.dumps(labelsGender),
                'dataGender': json.dumps(dataGender)})
    return render(request, 'reporting/test.html', context)

def StatistikGender(request):
    template = 'reporting/statistik/unit.html'
    model = TempDataLengkap092022
    query = model.objects.all().values('esl1').annotate(
        pria=Count(Case(When(kodekelamin='P', then=1), output_field=IntegerField(),)),
        wanita=Count(Case(When(kodekelamin='W', then=1), output_field=IntegerField(),)),
        jumlah=Count('kodekelamin'),
    ).order_by('esl1')
    jumlah = model.objects.all().values('kodekelamin').annotate(
        allPria=Count(Case(When(kodekelamin='P', then=1), output_field=IntegerField(),)),
        allWanita=Count(Case(When(kodekelamin='W', then=1), output_field=IntegerField(),)),
    )
    
    for a in jumlah:
        if a['kodekelamin'] == 'W':
            allWanita = a['allWanita']
        elif a['kodekelamin'] == 'P':
            allPria = a['allPria']
        else:
            semua = a['semua']
            
    #print(jumlah)
    context = ({'query': query, 'allWanita': allWanita, 'allPria': allPria})
    return render(request, template, context)

def StatistikGolongan(request):
    template = 'reporting/statistik/golongan.html'
    model = TempDataLengkap092022
    query = model.objects.all().values('esl1').annotate(
        i_a=Count(Case(When(kodegolonganruang='I/a', then=1), output_field=IntegerField(),)),
        i_b=Count(Case(When(kodegolonganruang='I/b', then=1), output_field=IntegerField(),)),
        i_c=Count(Case(When(kodegolonganruang='I/c', then=1), output_field=IntegerField(),)),
        i_d=Count(Case(When(kodegolonganruang='I/d', then=1), output_field=IntegerField(),)),
        ii_a=Count(Case(When(kodegolonganruang='II/a', then=1), output_field=IntegerField(),)),
        ii_b=Count(Case(When(kodegolonganruang='II/b', then=1), output_field=IntegerField(),)),
        ii_c=Count(Case(When(kodegolonganruang='II/c', then=1), output_field=IntegerField(),)),
        ii_d=Count(Case(When(kodegolonganruang='II/d', then=1), output_field=IntegerField(),)),
        iii_a=Count(Case(When(kodegolonganruang='III/a', then=1), output_field=IntegerField(),)),
        iii_b=Count(Case(When(kodegolonganruang='III/b', then=1), output_field=IntegerField(),)),
        iii_c=Count(Case(When(kodegolonganruang='III/c', then=1), output_field=IntegerField(),)),
        iii_d=Count(Case(When(kodegolonganruang='III/d', then=1), output_field=IntegerField(),)),
        iv_a=Count(Case(When(kodegolonganruang='IV/a', then=1), output_field=IntegerField(),)),
        iv_b=Count(Case(When(kodegolonganruang='IV/b', then=1), output_field=IntegerField(),)),
        iv_c=Count(Case(When(kodegolonganruang='IV/c', then=1), output_field=IntegerField(),)),
        iv_d=Count(Case(When(kodegolonganruang='IV/d', then=1), output_field=IntegerField(),)),
        iv_e=Count(Case(When(kodegolonganruang='IV/e', then=1), output_field=IntegerField(),)),
        jumlah=Count('kodegolonganruang'),
    ).order_by('esl1')
    context = ({'query': query, })
    return render(request, template, context)

def StatistikPendidikan(request):
    template = 'reporting/statistik/pendidikan.html'
    model = TempDataLengkap092022
    query = model.objects.all().values('esl1').annotate(
        sd=Count(Case(When(singkatanjenjang='SD', then=1), output_field=IntegerField(),)),
        smp=Count(Case(When(singkatanjenjang='SMP', then=1), output_field=IntegerField(),)),
        sma=Count(Case(When(singkatanjenjang='SMA', then=1), output_field=IntegerField(),)),
        d1=Count(Case(When(singkatanjenjang='D1', then=1), output_field=IntegerField(),)),
        d2=Count(Case(When(singkatanjenjang='D2', then=1), output_field=IntegerField(),)),
        d3=Count(Case(When(singkatanjenjang='D3', then=1), output_field=IntegerField(),)),
        d4=Count(Case(When(singkatanjenjang='D4', then=1), output_field=IntegerField(),)),
        s1=Count(Case(When(singkatanjenjang='S1', then=1), output_field=IntegerField(),)),
        s2=Count(Case(When(singkatanjenjang='S2', then=1), output_field=IntegerField(),)),
        s3=Count(Case(When(singkatanjenjang='S3', then=1), output_field=IntegerField(),)),
    ).order_by('esl1')
    context = ({'query': query, })
    return render(request, template, context)

def petaSebaranPegawai(request):
    template = 'reporting/statistik/peta.html'
    model = TempDataLengkap092022
    
    data = []
    query = model.objects.all().values('provinsikantor').annotate(
        jumlah = Count('idpegawai')
    ).order_by('provinsikantor')
    
    contex = ({'query': query, 'json_data': json.dumps(data)})
    return render(request, template, contex)