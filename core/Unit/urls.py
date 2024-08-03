from django.urls import path

from . import views

urlpatterns = [
    path('unit/', views.UnitSet.as_view()),
    path('unit-photo/', views.UnitPhotoSet.as_view()),
    path('unit-detail/', views.UnitDetailSet.as_view()),
]