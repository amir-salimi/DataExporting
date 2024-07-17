from django.urls import path

from . import views

urlpatterns = [
    path('city-prop/', views.CityProperties.as_view()),
    path('lat-long/', views.GetLatLong.as_view()),
    path('building/', views.BuildingSet.as_view()),
    path('building-unit/', views.BuildingUnit.as_view()),
    path('complite-building/', views.CompliteBuilding.as_view()),
]