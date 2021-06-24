from django.db import models
from django.db.models.fields import CharField

class Patient(models.Model):
    Name = models.CharField(max_length=122)
    Age = models.IntegerField()
    Blood_Group = models.CharField(max_length=5)

