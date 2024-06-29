from typing import Any
import requests 

from django.shortcuts import render
from django.db.models import Q, F
from django.http import HttpRequest, HttpResponse
from django.views.generic import DetailView, CreateView

from .models import City, Area, Community, Part, Building, Detail, BuildingImg, BuildingStatus, Highlight, UnitDetail, UnitOfBuilding, UnitPhoto
from .filter import ProductFilter

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
    

class BuildingSet(CreateView):
    def get(self, request):
        name = request.GET.get("name", None)
        link = request.GET.get("link", None)
        highlight = request.GET.get("highlight", None)
        img_link = request.GET.get("img", None)
        key = request.GET.get("key", None)
        value = request.GET.get("value", None)
        status = request.GET.get("status", None)
        location = request.GET.get("location", None)
        about = request.GET.get("about", None)

        if link and highlight:
            Highlight.objects.get_or_create(link=link, highlight=highlight)
        
        if link and img_link:
            BuildingImg.objects.get_or_create(link=link, img_link=img_link)
        
        if link and key and value:
            Detail.objects.get_or_create(link=link, key=key, value=value)

        if link and status and name and location and about:
            highlights = Highlight.objects.filter(link=link)
            buildingImgs = BuildingImg.objects.filter(link=link)
            details = Detail.objects.filter(link=link)
            try:
                building, building_created = Building.objects.get_or_create(name=name, link=link, status=status, location=location, about=about)
                
                for highlight in highlights:
                    building.highlight.add(highlight)
                    building.save()

                for img in buildingImgs:
                    building.img_link.add(img)
                    building.save()

                for detail in details:
                    building.details.add(detail)
                    building.save()
            except:
                pass
            

        return HttpResponse("ok")
    

class BuildingUnit(CreateView):
    def get(self, request):
        link = request.GET.get("link", None)
        key = request.GET.get("key", None)
        value = request.GET.get("value", None)
        img = request.GET.get("img", None)
        ok = request.GET.get("is_ok", None)

        building_name = request.GET.get("building_name", None)

        community = request.GET.get("community", None)
        area = request.GET.get("area", None)
        city = request.GET.get("city", None)
        bed = request.GET.get("bed", None)
        bath = request.GET.get("bath", None)
        price = request.GET.get("price", None)
        unit_area = request.GET.get("unit_area", None)
        description = request.GET.get("description", None)

        building_link = request.GET.get("building_link", None)
        
        if building_link or building_name:
            if ok :
                building = ProductFilter(building_name, Building.objects.all()).data
                
                if building:
                    building = Building.objects.filter(Q(name__iexact=building) | Q(link=building_link)).first()
                else:
                    building = Building.objects.filter(Q(name__iexact=building_name) | Q(link=building_link)).first()

                building.is_ok=1
                building.save()

        if link and key and value :
            UnitDetail.objects.get_or_create(link=link, key=key, value=value)
        
        if link and img:
            UnitPhoto.objects.get_or_create(link=link, img_link=img)


        if building_name or building_link:
            if price and bath and bed and link:
                building = ProductFilter(building_name, Building.objects.all()).data
                print(building)

                if building:
                    building = Building.objects.filter(Q(name__iexact=building) | Q(link=building_link)).first()
                else:
                    building = Building.objects.filter(Q(name__iexact=building_name) | Q(link=building_link)).first()

                
                unit, unit_created = UnitOfBuilding.objects.get_or_create(link=link, building_name=building, bed=bed, bath=bath, area=unit_area, desc=description)

                photos = UnitPhoto.objects.filter(link=link)
                details = UnitDetail.objects.filter(link=link)
            
                for p in photos:
                    unit.photo.add(p)
                    unit.save()

                for d in details:
                    unit.detail.add(d)
                    unit.save()

                building.city = city
                building.area = area
                building.community = community
                building.save()



        return HttpResponse()

