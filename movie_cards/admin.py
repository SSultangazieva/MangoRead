from django.contrib import admin
from movie_cards.models import Movie, Review, Genre, Type

class MovieAdmin(admin.ModelAdmin):
    list_display = ['title', 'description'] #выводятся эти поля
    search_fields = ['title'] #поиск по названию
    list_filter = ['types', 'genres'] #фильтрация по этим полям

admin.site.register(Movie, MovieAdmin)
admin.site.register(Review)
admin.site.register(Genre)
admin.site.register(Type)
