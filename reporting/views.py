from django.shortcuts import render
from django.http import HttpResponse
from .models import TempDataLengkap092022
from django.db.models import Count, Case, When, IntegerField

# Create your views here.
def test(request):
    return render(request, 'reporting/test.html')

def StatistikGender(request):
    template = 'reporting/statistik/unit.html'
    model = TempDataLengkap092022
    query = model.objects.all().values('esl1').annotate(
        pria=Count(Case(When(kodekelamin='P', then=1), output_field=IntegerField(),)),
        wanita=Count(Case(When(kodekelamin='W', then=1), output_field=IntegerField(),)),
        jumlah=Count('kodekelamin'),
    ).order_by('esl1')
    context = ({'query': query})
    return render(request, template, context)

