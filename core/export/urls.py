from django.urls import path

from . import views

urlpatterns = [
    path('opr-data/', views.OprScrapingData.as_view()),
    path('dxb-data/', views.DxbScrapingData.as_view()),
    path('easymap-data/', views.EasyMapScraping.as_view()),
]