from django.urls import path
from . import views

urlpatterns = [
    path('building/', views.BuildingSet.as_view()),
    path('merg-duplicate-buildings/', views.MergDuplicateBuilding.as_view()),
    path('update-buildings/', views.UpdateBuildings.as_view()),
]