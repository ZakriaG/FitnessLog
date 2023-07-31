from django.db import models


# Create your models here.

class WorkOutLog(models.Model):
    # name of the exercise:
    name = models.CharField(max_length=200)
    # Weight in kg:
    weight = models.IntegerField()

    def __str__(self):
        return self.name
