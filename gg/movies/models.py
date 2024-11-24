from django.db import models

class Actor(models.Model):
    name = models.CharField(max_length=50)
    poster_path = models.CharField(max_length=200, blank= True, null= True)

class Genre(models.Model):
    name = models.CharField(max_length=50) 

class Movie(models.Model):
    title = models.CharField(max_length=100)
    release_date = models.DateField(blank=True)  
    popularity = models.FloatField()
    vote_count = models.IntegerField()  
    vote_average = models.FloatField()  
    overview = models.TextField()
    runtime = models.IntegerField() 
    production_country = models.CharField(max_length=100)  
    poster_path = models.CharField(max_length=200, blank=True)   #이미지
    backdrop_path = models.CharField(max_length=200)
    genres = models.ManyToManyField(Genre, blank=True)
    youtube_key = models.CharField(max_length=100, blank=True)
    actors = models.ManyToManyField(Actor, blank= True)
    director = models.CharField(max_length=100, blank=True)
    words = models.CharField(max_length=255, blank=True)