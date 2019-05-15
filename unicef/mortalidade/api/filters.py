import django_filters

from mortalidade.models import Paciente


class CountryFilter(django_filters.FilterSet):
    nome = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = Country
        fields = ['nome']