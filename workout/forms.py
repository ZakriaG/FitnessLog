from django import forms
from django.core.exceptions import ValidationError


class CreateNewWorkoutLog(forms.Form):
    ExerciseName1 = forms.CharField(max_length=200)
    Set1Weight1 = forms.IntegerField(required=True, error_messages={
            'required': 'Enter kg for set 1'
        })
    Set2Weight1 = forms.IntegerField(required=True, error_messages={
            'required': 'Enter kg for set 2'
        })
    Set3Weight1 = forms.IntegerField(required=True, error_messages={
            'required': 'Enter kg for set 3'
        })
    Set4Weight1 = forms.IntegerField(required=True, error_messages={
            'required': 'Enter kg for set 4'
        })

    ExerciseName2 = forms.CharField(max_length=200)
    Set1Weight2 = forms.IntegerField(required=True, error_messages={
            'required': 'Enter kg for set 1'
        })
    Set2Weight2 = forms.IntegerField(required=True, error_messages={
            'required': 'Enter kg for set 2'
        })
    Set3Weight2 = forms.IntegerField(required=True, error_messages={
            'required': 'Enter kg for set 3'
        })
    Set4Weight2 = forms.IntegerField(required=True, error_messages={
                                    'required': 'Enter kg for set 4' }
                                     )