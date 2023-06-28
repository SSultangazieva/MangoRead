from rest_framework import serializers

from movie_cards.models import(
    Type,
    Genre,
    Movie,
    Review,)

class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        exclude = ['id']

class GenresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['name']

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        exclude = ['id']

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        exclude = ['id']

class MovieDetailSerializer(serializers.ModelSerializer):
    movie_reviews = ReviewSerializer(many=True)
    types_name = TypeSerializer(many=True)
    genres_name = GenresSerializer(many=True)

    class Meta:
        model = Movie
        fields = ['photo', 'title', 'description', 'types_name', 'genres_name', 'year', 'movie_reviews']

