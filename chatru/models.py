from django.db import models

# Create your models here.


class Translation(models.Model):
    texto = models.TextField()


