from django.urls import path
from . import views

urlpatterns = [
    path('', views.PenguinController.as_view()),
]