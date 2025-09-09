from django.urls import path
from . import views

urlpatterns = [
    path("auth/register/", views.RegisterView.as_view()),
    path("profile/", views.UserProfileView.as_view()),
]
