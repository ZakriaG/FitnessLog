from django.urls import path
from . import views

urlpatterns = [
    path('', views.myview),
    path('meal', views.meal, name="meal"),
    path('workout', views.workout, name="workout")
]