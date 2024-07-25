from django.urls import path

from . import views

urlpatterns = [
    path('building-unit/', views.BuildingUnit.as_view()),

]