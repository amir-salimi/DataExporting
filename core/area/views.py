import requests 

from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import DetailView, CreateView

from .models import City, Area, Community, Part

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
        part = request.GET.get("part", None) 
        source = request.GET.get("source", None) 

        city, city_created = City.objects.get_or_create(city=city, source=source)

        if area is not None:
            area, area_created = Area.objects.get_or_create(area=area, city=city, source=source)
            if community is not None:
                community, community_created = Community.objects.get_or_create(area=area, community=community, source=source)
                if part is not None:
                    part, part_created = Part.objects.get_or_create(community=community, part=part, source=source)
        return HttpResponse("ok")
    


class GetLatLong(CreateView):
    def get(self, request):
        city = request.GET.get("city", None)
        print(city)
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