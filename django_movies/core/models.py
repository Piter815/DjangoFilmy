from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=20, unique=True)
    age_limit = models.IntegerField(null=True)

    def __str__(self):
        return self.name


class Countries(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name


class Director(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)



    def __str__(self):
        return f'{self.name}, {self.surname}'


class Movies(models.Model):
    title = models.CharField(max_length=100)
    rating = models.IntegerField(null=True, validators=[MaxValueValidator(10), MinValueValidator(1)])
    released = models.DateField()
    description = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    genre = models.ForeignKey(Genre, null=True, on_delete=models.DO_NOTHING)
    country = models.ForeignKey(Countries, null=True, on_delete=models.DO_NOTHING)
    director = models.ForeignKey(Director, null=True, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f'{self.title} from {self.released}'