from django.urls import path

from movie_cards.views import (
    MovieViewSet,
    MovieDetailViewSet,
    ReviewViewSet
)

urlpatterns = [
    path("movie/", MovieViewSet.as_view({'get': 'list'}), name="КАрточки"),
    path("movie/<int:id>/", MovieDetailViewSet.as_view({'get': 'retrieve'}), name="Карточки по ID"),
    path("reviews/", ReviewViewSet.as_view({'get': 'list', 'post': 'create'}), name="Рецензии"),
]