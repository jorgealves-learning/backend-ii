from django.db import models


# Create your models here.
# movie publisher
class Publisher(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# movie
class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    release_date = models.DateField()
    publisher = models.ForeignKey(
        Publisher, related_name="movies", on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title


# movie actor
class Actor(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    movies = models.ManyToManyField(Movie, related_name="actors")

    def __str__(self):
        return self.name


# tvshow
class TVShow(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    release_date = models.DateField()
    publisher = models.ForeignKey(
        Publisher, related_name="tvshows", on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title
