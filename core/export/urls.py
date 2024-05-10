from django.urls import path

from . import views

urlpatterns = [
    path('data/', views.GetData.as_view())
]