from rest_framework import viewsets

from mortalidade.models import *
from mortalidade.api.serializers import *
#from mortalidade.api.filters import CountryFilter


class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
   

class MortalityViewSet(viewsets.ModelViewSet):
    queryset = Mortality.objects.all()
    serializer_class = MortalitySerializer

