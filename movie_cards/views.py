from rest_framework import viewsets
from .models import Movie, Review, Genre, Type
from .serializers import MovieSerializer,MovieDetailSerializer,GenresSerializer,TypeSerializer,ReviewSerializer
from django_filters.rest_framework import DjangoFilterBackend
from movie_cards.filters import MoviesFilter
from rest_framework import generics, filters, pagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.pagination import PageNumberPagination


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_backends = [
        DjangoFilterBackend,  # сама фильтрация
        filters.SearchFilter,  # через поисковик
    ]
    filterset_class = (MoviesFilter)
    filterset_fields = [
        "title",
        "genres",
        "types",
        "year",
    ]
    search_fields = ["title"]  # через поисковик
    pagination_class = pagination.PageNumberPagination


class MovieDetailViewSet(viewsets.ModelViewSet):
    lookup_field = 'id'
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    # permission_classes = [IsAuthenticatedOrReadOnly]



