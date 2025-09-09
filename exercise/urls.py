from django.urls import path
from . import views

urlpatterns = [
    path("exercises/", views.ExerciseListCreateView.as_view()),
    path("exercises/<int:pk>/", views.ExerciseDetailView.as_view()),

    path("routines/", views.RoutineListCreateView.as_view()),
    path("routines/<int:pk>/", views.RoutineDetailView.as_view()),
    
    path("routines/users/<int:user_id>/", views.UserRoutinesView.as_view())
]
