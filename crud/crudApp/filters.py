import django_filters
from .models import Autor, Genero, Livros

class LivrosFilter(django_filters.FilterSet):
    titulo = django_filters.CharFilter(lookup_expr='icontains', label="Titulo")
    autor = django_filters.ModelChoiceFilter(queryset=Autor.objects.all(), label= 'Autor')
    genero = django_filters.ModelChoiceFilter(queryset=Genero.objects.all(), label='Gênero')
    preco_min = django_filters.NumberFilter(field_name='preco', lookup_expr='gte', label='Preço Mínimo')
    preco_max = django_filters.NumberFilter(field_name='preco', lookup_expr='lte', label='Preço Máximo')

    class Meta:
        model = Livros
        fields = ['titulo', 'autor', 'genero', 'preco_min', 'preco_max']

