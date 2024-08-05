from datetime import datetime

from django.shortcuts import render
from django.views.generic import DetailView
from django.db.models import Q
from django.http import HttpResponse

from rest_framework.viewsets import generics, ModelViewSet
from rest_framework import status
from rest_framework.response import Response

from .models import Building, BuildingDetail, BuildingImg, BuildingHighlight, Complex
from .serializers import (
    UpdateComplexPublishStatusModelSerializer, BuildingHighlightModelSerializer, BuildingImgModelSerializer, 
    BuildingDetailModelSerializer, BuildingModelSerializer, ComplexModelSerializer
    )


class HttpResponseOk(HttpResponse):
    status_code = 200


class UpdateComplexPublishStatusViewSet(generics.UpdateAPIView):
    queryset = Complex.objects.all()
    serializer_class = UpdateComplexPublishStatusModelSerializer


class BuildingHighlightViewSet(generics.CreateAPIView):
    queryset = BuildingHighlight.objects.all()
    serializer_class = BuildingHighlightModelSerializer


class BuildingImgViewSet(generics.CreateAPIView):
    queryset = BuildingImg.objects.all()
    serializer_class = BuildingImgModelSerializer


class BuildingDetailViewSet(generics.CreateAPIView):
    queryset = BuildingDetail.objects.all()
    serializer_class = BuildingDetailModelSerializer


class BuildingViewSet(ModelViewSet):
    queryset = Building.objects.all()
    serializer_class = BuildingModelSerializer 


class ComplexViewSet(ModelViewSet):
    queryset = Complex.objects.all()
    serializer_class = ComplexModelSerializer

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()

        if request.data.get("buildings", None) != None:
            instance.buildings.add(*Building.objects.filter(pk__in=request.data["buildings"]))
            instance.save()
            return Response(status=status.HTTP_200_OK)
        
        elif request.data.get("publish_status", None) != None:
            instance.publish_status = int(request.data.get("publish_status"))
            instance.save()
            return Response(status=status.HTTP_200_OK)
    
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    
    
class MergDuplicateBuilding(DetailView):
    def get(self, request):
        not_complite_buildings = Building.objects.filter(Q(building_link=None) or Q(building_link=" "))
        for not_complite_building in not_complite_buildings:
            complite_building = Building.objects.filter(Q(name=not_complite_building.name) & Q(publish_status=1)).first()
            if complite_building != None:
                not_complite_building.building_link = complite_building.building_link
                not_complite_building.status = complite_building.status
                not_complite_building.location = complite_building.location
                not_complite_building.about = complite_building.about
                not_complite_building.created_time = datetime.now()
                not_complite_building.publish_status = 2
                not_complite_building.save()
                complite_building.delete()
                
        return HttpResponseOk()
    


    
    