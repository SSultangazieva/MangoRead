from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Type(models.Model):
    name = models.CharField(max_length=100, verbose_name="Тип:")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тип"
        verbose_name_plural = "Типы"

class Genre(models.Model):
    name = models.CharField(max_length=100, verbose_name="Жанр:")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"


class Movie(models.Model):
    photo = models.ImageField(
        upload_to="media/",
        blank=True,
        verbose_name="Картинка",
    )
    title = models.CharField(max_length=100, verbose_name="Название")
    description = models.TextField(null=True, blank=True,  verbose_name="Описание")
    types = models.ManyToManyField(Type, related_name="film_type", verbose_name="Тип_фильма")
    genres = models.ManyToManyField(Genre, related_name="film_genre", verbose_name="Жанр_фильма", blank=True)
    year = models.IntegerField(validators=[MinValueValidator(1900), MaxValueValidator(2050)],verbose_name='Год выпуска')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Фильм"
        verbose_name_plural = "Фильмы"

class Review(models.Model):
    movie_reviews = models.ForeignKey(Movie,on_delete=models.CASCADE, related_name="movie_reviews", verbose_name="рецензия yf abkmv",)
    # user = models.ForeignKey("users.User", on_delete=models.CASCADE, null=True, related_name="user_reviews")
    text = models.TextField(verbose_name="Рецензии")
    # stars = models.IntegerField(choices=review_stars, verbose_name="Звёзды")
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Рецензия"
        verbose_name_plural = "Рецензии"
