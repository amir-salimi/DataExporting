from django.urls import path

from . import views

urlpatterns = [
    path('city-prop/', views.CityProperties.as_view()),
    path('lat-long/', views.GetLatLong.as_view())
]