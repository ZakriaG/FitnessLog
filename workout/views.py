from django.shortcuts import render
from .forms import CreateNewWorkoutLog
from .models import WorkOutLog
from django.core.exceptions import ValidationError
import re

# Create your views here.
def myview(request):
    return render(request, "./home/index.html")


def meal(request):
    return render(request, "./meal/index.html")


def workout(request):
    return render(request, "./workout/baseWorkout.html")


def workout_monday(request):
    form = CreateNewWorkoutLog(request.POST)
    if request.method == "POST":

        if form.is_valid():
            form_data = form.cleaned_data
            ExerciseName = request.POST.get('ExerciseName')
            for set in form_data:
                if set.startswith('Set'):
                    SetNumber = re.findall(r'\d', set)[0]
                    Weight=form_data[set]
                    w = WorkOutLog(ExerciseName=ExerciseName,
                                   SetNumber=SetNumber,
                                   Weight=Weight)
                    w.save()
        else:
            print('her 1')
            return render(request, "./workout/monday.html", {"workout_form": form})
    else:
        print('her')
        form = CreateNewWorkoutLog()

    print('her2')
    return render(request, "./workout/monday.html", {"workout_form": form})


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
