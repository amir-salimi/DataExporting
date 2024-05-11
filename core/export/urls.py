from django.urls import path

from . import views

urlpatterns = [
    path('opr_data/', views.OprScrapingData.as_view()),
    path('data/', views.DxbScrapingData.as_view()),

]