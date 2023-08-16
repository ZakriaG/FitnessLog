from django import forms
from django.core.exceptions import ValidationError


class CreateNewWorkoutLog(forms.Form):
    ExerciseName = forms.CharField(max_length=200)
    Set1Weight = forms.IntegerField(error_messages={
            'required': 'Enter kg for set 1'
        })
    Set2Weight = forms.IntegerField(error_messages={
            'required': 'Enter kg for set 2'
        })
    Set3Weight = forms.IntegerField(error_messages={
            'required': 'Enter kg for set 3'
        })
    Set4Weight = forms.IntegerField(error_messages={
            'required': 'Enter kg for set 4'
        })