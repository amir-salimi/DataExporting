import requests 

from datetime import datetime

from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.db.models import Q
from django.http import HttpResponse
from django.views.generic import DetailView, CreateView

from .models import City, Area, Community
from Building.models import Building, Complex


class HttpResponseOk(HttpResponse):
    status_code = 200


def edit_svg(svg):
    svg = svg.replace("L", "")
    svg = svg.replace("M", "")
    svg = svg.replace("Z", "")
    svg = svg.split(" ")
    svg = ' '.join(svg).split()
    return svg


class CityProperties(DetailView):
    def get(self, request):
        city = request.GET.get("city", None)
        area = request.GET.get("area", None) 
        community = request.GET.get("community", None) 
        building_name = request.GET.get("building", None) 
        source = request.GET.get("source", None) 
        subnet = request.GET.get("subnet", None)
        about = request.GET.get("about", None)

        city, city_created = City.objects.get_or_create(name=str(city).lower())

        if building_name and community and area and city is not None:
            area, area_created = Area.objects.get_or_create(city=city, name=str(area).lower(), source=source)
            community, community_created = Community.objects.get_or_create(name=str(community).lower(), area=area, city=city, source=source)

            if subnet is None: # if the building is not in a complex 
                building = Building.objects.create(community=community, name=str(building_name).lower(), source=source, area=area, city=city, about=None)

            else: # if the building is in a complex 
                complex, complex_created = Complex.objects.get_or_create(name=str(building_name), source=source)
                building = Building.objects.create(community=community, name=str(subnet).lower(), source=source, area=area, city=city)
                complex.area = area
                complex.city = city
                complex.community = community
                complex.created_time = datetime.now()
                complex.save()
                complex.buildings.add(building)
                

        if building_name and area and city is not None:
            if community == None:
                area, area_created = Area.objects.get_or_create(city=city, name=str(area).lower(), source=source)
                building = Building.objects.create(name=str(building_name).lower(), source=source, area=area, city=city)
        
        if building_name and city is not None:
            if community and area is None:
                building = Building.objects.create(name=str(building_name).lower(), source=source, city=city)

        return HttpResponseOk()
    

class GetLatLong(CreateView):
    def get(self, request):

        city = request.GET.get("city", None)
        url = f"https://nominatim.openstreetmap.org/search?city={city}&format=json&addressdetails=1&limit=1&polygon_svg=1"
        a = requests.get(url).json()
        svg = a[0]["svg"]
        svg = edit_svg(svg)
        svg = svg[::-1]
        svg = [i.replace("-", "") for i in svg]
        LatLong = []
        for i in range(0, len(svg), 2):
            LatLong.append([svg[i], svg[i+1]])
        return HttpResponse(LatLong)


