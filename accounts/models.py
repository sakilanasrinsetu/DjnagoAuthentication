from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length = 250)
    section = models.CharField(max_length = 250)
    roll = models.CharField(max_length = 250)

    def __str__(self):
        return self.name