from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
# def football_pic(models.Model):
class Player(models.Model):
    name = models.CharField(max_length=50)
    thumbnail  = models.CharField(max_length=250)
    pic = models.CharField(max_length=250)
    player_team = models.CharField(max_length=100)
    age = models.IntegerField(validators=[MinValueValidator(15)])
    height_M = models.FloatField(validators=[MinValueValidator(0)])
    weight_Kg = models.FloatField(validators=[MinValueValidator(0)])

    def __str__(self):
        return self.name

    
