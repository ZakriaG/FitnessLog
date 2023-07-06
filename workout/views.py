from django.shortcuts import render

# Create your views here.
def myview(request):
    return render(request, "./home/index.html")

def meal(request):
    return render(request, "./meal/index.html")

def workout(request):
    return render(request, "./workout/index.html")

def workout_monday(request):
    return render(request, "./workout/monday.html")

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