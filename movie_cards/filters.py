from django_filters import rest_framework as filters, ModelChoiceFilter
from movie_cards.models import Genre,Type

class MoviesFilter(filters.FilterSet):
    genres = ModelChoiceFilter(queryset=Genre.objects.all())
    types = ModelChoiceFilter(queryset=Type.objects.all())
    year = filters.RangeFilter(field_name="year")