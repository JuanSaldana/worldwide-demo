from django.db import models

# Create your models here.


class Song(models.Model):
    name = models.CharField(max_length=50)


class Artist(models.Model):
    artistic_name = models.CharField(max_length=50)
    songs = models.ManyToManyField(Song)
