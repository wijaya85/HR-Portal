from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import TempDataLengkap092022, Statistikpegawaiperuniteselon1
from pegawai.models import DataLengkap
from django.db.models import Count, Case, When, IntegerField
import json

# Create your views here.    
    
def test(request):
    labelsGender = []
    dataGender = []
    labelsGolongan = []
    dataGolongan = []
    labelPendidikan = []
    dataPendidikan = []
    model = DataLengkap
    gender = model.objects.all().values('kodekelamin').annotate(
        jumlah=Count('idpegawai'),
    ).order_by('kodekelamin')
    
    golongan = model.objects.all().values('kodegolongan').annotate(
        jumlah=Count('idpegawai')
    ).order_by('kodegolongan')
    
    pendidikan = model.objects.all().values('singkatanjenjang').annotate(
        jumlah=Count('idpegawai')
    ).order_by('singkatanjenjang')
    
    for b in gender:
        labelsGender.append(b['kodekelamin'])
        dataGender.append(b['jumlah'])
    
    for a in golongan:
        labelsGolongan.append(a['kodegolongan'])
        dataGolongan.append(a['jumlah'])
        
    for c in pendidikan:
        labelPendidikan.append(c['singkatanjenjang'])
        dataPendidikan.append(c['jumlah'])
        
    context = ({'labels': json.dumps(labelsGender), 
                'values':json.dumps(dataGender),
                'golLabels': json.dumps(labelsGolongan),
                'golValues': json.dumps(dataGolongan),
                'pendidikanLabels': json.dumps(labelPendidikan),
                'pendidikanValues': json.dumps(dataPendidikan),})
    return render(request, 'reporting/test.html', context)


def StatistikGender(request):
    template = 'reporting/statistik/unit.html'
    model = DataLengkap
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
    model = DataLengkap
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
    model = DataLengkap
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
    model = DataLengkap
    
    provinsi = []
    jumlah = []
    data = []
    query = model.objects.all().values('provinsikantor').annotate(
        jumlah = Count('idpegawai')
    ).order_by('provinsikantor')
    
    #for q in query:
    #    data.append(q['provinsikantor'] + ":" + str(q['jumlah']))
    
    data = [{data['provinsikantor']:data['jumlah']} for data in query]
    
    print(data)
    contex = ({'query': query, 'provinsi': json.dumps(provinsi), 'jumlah': json.dumps(jumlah), 'data': data})
    return render(request, template, contex)