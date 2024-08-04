from django.shortcuts import render
from django.views.generic import CreateView, DetailView, UpdateView
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from django.http import HttpResponse
from datetime import datetime

from rest_framework.viewsets import generics

from .models import Building, BuildingDetail, BuildingImg, BuildingHighlight, Complex
from area.models import Area, Community, City

from .serializers import UpdateBuildingDetailModelSerializer, UpdateComplexPublishStatusModelSerializer, BuildingHighlightModelSerializer, BuildingImgModelSerializer, BuildingDetailModelSerializer


class HttpResponseOk(HttpResponse):
    status_code = 200


class UpdateBuildingDetailsViewSet(generics.UpdateAPIView):
    queryset = Building.objects.all()
    serializer_class = UpdateBuildingDetailModelSerializer


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


class BuildingViewSet(CreateView):
    def get(self, request):
        name = request.GET.get("name", None)
        link = request.GET.get("link", None)
        status = request.GET.get("status", None)
        area = request.GET.get("location", None)
        about = request.GET.get("about", None)
        city = request.GET.get("city", None)
        complex_name = request.GET.get("complex_name", None)

        if about == "None":
            about = None



        if link and name and area and about:
            City.objects.get_or_create(name=str(city).lower())
            # if location was same with city we check that in this line 
            try: 
                building_city = City.objects.filter(name__iexact=area).get()
                building = Building.objects.create(name=str(name).lower(), building_link=link, status=str(status).lower(), location=str(area).lower(), about=about, city=building_city, publish_status=1)    

            except ObjectDoesNotExist:
                building_city, building_city_created = City.objects.get_or_create(name=str(city).lower())
                building_area, building_area_created = Area.objects.get_or_create(name=str(area).lower(), city=building_city)
                building = Building.objects.create(name=str(name).lower(), building_link=link, status=str(status).lower(), location=str(area).lower(), about=about, area=building_area, city=building_city, publish_status=1)    

            if complex_name is not None:
                complex = Complex.objects.filter(name__iexact=complex_name).first()
                complex.buildings.add(building)

            highlights = BuildingHighlight.objects.filter(building_link=link)
            buildingImgs = BuildingImg.objects.filter(building_link=link)
            details = BuildingDetail.objects.filter(building_link=link)

            building.highlight.add(*highlights)
            building.img_link.add(*buildingImgs)
            building.details.add(*details)
            

        return HttpResponseOk()
    
    
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
    


    
    