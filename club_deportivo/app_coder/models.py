from django.db import models

# Create your models here.

class Sport(models.Model):
    sport = models.CharField(max_length=40)
    id_sport = models.IntegerField()


class Profesor(models.Model):
    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    sport = models.CharField(max_length=30)
    num_id = models.IntegerField()
    email = models.EmailField()


class Partner(models.Model):
    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    num_id = models.IntegerField()
    email = models.EmailField()