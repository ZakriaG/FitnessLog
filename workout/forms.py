from django import forms


class CreateNewWorkoutLog(forms.Form):
    ExerciseName = forms.CharField(max_length=200)
    Set1Weight = forms.IntegerField()
    Set2Weight = forms.IntegerField()
    Set3Weight = forms.IntegerField()
    Set4Weight = forms.IntegerField()
