from django.urls import path

from . import views

urlpatterns = [
    path("agency/", views.AgencySet.as_view()),
    path("agent/", views.AgentSet.as_view()),
]
