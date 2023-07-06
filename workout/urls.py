from django.urls import path
from . import views

urlpatterns = [
    path('', views.myview),
    path('meal', views.meal, name="meal"),
    path('workout', views.workout, name="workout"),
    path('workout/monday', views.workout_monday, name="workout_monday"),
    path('tuesday', views.workout_tuesday, name="workout_tuesday"),
    path('workout', views.workout_tuesday, name="workout_wednesday"),
    path('workout', views.workout_thursday, name="workout_thursday"),
    path('workout', views.workout_friday, name="workout_friday"),
    path('workout', views.workout_saturday, name="workout_saturday"),
    path('workout', views.workout_sunday, name="workout_sunday")

]