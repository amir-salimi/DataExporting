from django.urls import path, include

from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()
router.register(r'building', views.BuildingViewSet)


urlpatterns = [
    path('', include(router.urls)),

    path('complex/', views.ComplexViewSet.as_view()),
    path('merg-duplicate-buildings/', views.MergDuplicateBuilding.as_view()),
    path('update-complex-publish-status/<int:pk>/', views.UpdateComplexPublishStatusViewSet.as_view()),
    path('building-image/', views.BuildingImgViewSet.as_view()),
    path('building-details/', views.BuildingDetailViewSet.as_view()),
    path('building-highlights/', views.BuildingHighlightViewSet.as_view()),
]