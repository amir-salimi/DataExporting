from django.urls import path
from . import views

urlpatterns = [
    path('building/', views.BuildingViewSet.as_view()),
    path('merg-duplicate-buildings/', views.MergDuplicateBuilding.as_view()),
    path('update-buildings/<int:pk>/', views.UpdateBuildingDetailsViewSet.as_view()),
    path('update-complex-publish-status/<int:pk>/', views.UpdateComplexPublishStatusViewSet.as_view()),
]