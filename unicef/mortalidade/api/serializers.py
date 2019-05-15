from rest_framework import serializers

from mortalidade.models import *


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ('iso_code', 'country_name')

class MortalitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Mortality
        fields = ('median', 'year', 'country')
