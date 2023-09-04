from django.shortcuts import render
from .forms import CreateNewWorkoutLog
from .models import WorkOutLog
from django.core.exceptions import ValidationError
import re
from django.template import Context, Template
from django.contrib import messages

# Create your views here.
def myview(request):
    return render(request, "./home/index.html")


def meal(request):
    return render(request, "./meal/index.html")


def workout(request):
    return render(request, "./workout/baseWorkout.html")


def workout_monday(request):
    newformName = ""
    ExerciseName = ""
    form=CreateNewWorkoutLog()
    if request.method == "POST":
        ExerciseName = [key for key in request.POST if key.endswith("-ExerciseName")][0].split("-")[0]
        print(f'ExerciseName = {ExerciseName}')
        form = CreateNewWorkoutLog(request.POST, prefix=ExerciseName)
        if form.is_valid():
            form_data = form.cleaned_data
            print(form_data)
            print(ExerciseName)
            for set in form_data:
                if set.startswith('Set'):
                    SetNumber = re.findall(r'\d', set)[0]
                    Weight=form_data[set]
                    w = WorkOutLog(ExerciseName=ExerciseName,
                                   SetNumber=SetNumber,
                                   Weight=Weight)
                    w.save()
            messages.success(request, f'Form submitted successfully.', extra_tags=ExerciseName)            #return render(request, "./workout/monday.html", {'form': form})
    else:
        form = CreateNewWorkoutLog()
    print(f'form = {form}')
    return render(request, "./workout/monday.html", {ExerciseName: form})


def workout_tuesday(request):
    return render(request, "./workout/tuesday.html")


def workout_wednesday(request):
    return render(request, "./workout/wednesday.html")


def workout_thursday(request):
    return render(request, "./workout/thursday.html")


def workout_friday(request):
    return render(request, "./workout/friday.html")


def workout_saturday(request):
    return render(request, "./workout/Saturday.html")


def workout_sunday(request):
    return render(request, "./workout/sunday.html")