from django.contrib import admin
from movie_cards.models import Movie,Review,Genre,Type
# Register your models here.

admin.site.register(Movie)
admin.site.register(Review)
admin.site.register(Genre)
admin.site.register(Type)