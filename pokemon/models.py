from django.db import models

# Create your models here.
class Pokemon(models.Model):
    class PokemonType(models.TextChoices):
      WATER = 'WA'
      GRASS = 'GR'
      GHOST = 'GH'
      STEEL = 'ST'
      FAIRY = 'FA'  

    name = models.CharField(max_length=30)
    type = models.CharField(choices=PokemonType.choices, max_length=150)
    hp = models.PositiveIntegerField()
    active = models.BooleanField()
    name_fr = models.CharField(max_length=30, default="")
    name_ar = models.CharField(max_length=30, default="")
    name_jr = models.CharField(max_length=30, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    
