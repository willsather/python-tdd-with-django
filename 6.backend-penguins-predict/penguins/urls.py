from django.urls import path
from . import views

urlpatterns = [
    path('', views.PenguinController.as_view()),
    path('<int:pk>/', views.PenguinDetailController.as_view()),
    path('predict/', views.PenguinPredictController.as_view()),
]
