from django.db import models


# Create your models here.

class WorkOutLog(models.Model):
    # name of the exercise:
    ExerciseName = models.CharField(max_length=200)

    # Weight in kg:
    Set1Weight = models.IntegerField()
    Set2Weight = models.IntegerField()
    Set3Weight = models.IntegerField()
    Set4Weight = models.IntegerField()
    # Time Stamp:
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
