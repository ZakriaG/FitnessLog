from django.shortcuts import render
from .forms import WorkoutLog

# Create your views here.
def myview(request):
    return render(request, "./home/index.html")


def meal(request):
    return render(request, "./meal/index.html")


def workout(request):
    return render(request, "./workout/baseWorkout.html")


def workout_monday(response):
    if response.method == "POST":
        form = WorkoutLog(response.POST)
        print("triggered")
        print(f"n={form}")
        #n = form.cleaned_data["weight"]ExerciseName
        ExerciseName = form.cleaned_data["ExerciseName"]
        Set1Weight = form.cleaned_data["Set1Weight"]
        Set2Weight = form.cleaned_data["Set2Weight"]
        Set3Weight = form.cleaned_data["Set3Weight"]
        Set4Weight = form.cleaned_data["Set4Weight"]
        print(f"ExerciseName={ExerciseName}")
        print(f"n={Set2Weight}")
        print(f"n={Set3Weight}")
        print(f"n={Set4Weight}")
        if form.is_valid():
            w = WorkOutLog(name=n, nweight=w)
            w.save()
        #return HttpResponseRedirect("/%i" %t.id)
    else:
        form = WorkoutLog()
    return render(response, "./workout/monday.html", {"form": form})


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
