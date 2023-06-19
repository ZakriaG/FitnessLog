from django.shortcuts import render

# Create your views here.
def myview(request):
    return render(request, "./home/index.html")

def meal(request):
    return render(request, "./meal/index.html")

def workout(request):
    return render(request, "./workout/index.html")