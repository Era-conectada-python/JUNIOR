from django.forms import ModelForm
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .models import *


def country_view(request):
	countries = Country.objects.all()
	return render(request, 'template/listagem.html', {'countries': countries})


def mortality_view(request):
     countries = Mortality.objects.all().exclude(median__exact="").values_list('country')[:30]
     mortalities = Mortality.objects.all().exclude(median__exact="")[:30]
     return render(request, 'template/listagem.html', {'mortalities': mortalities, 'countries': countries})

