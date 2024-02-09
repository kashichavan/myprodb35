from django.db import models

# Create your models here.
class Employee(models.Model):
    firstName=models.CharField(max_length=30)
    age=models.IntegerField(default=20)


