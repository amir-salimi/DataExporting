import requests 

from datetime import datetime

from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.db.models import Q, F
from django.http import HttpRequest, HttpResponse
from django.views.generic import DetailView, CreateView, UpdateView

from .models import City, Area, Community, Building, BuildingDetail, BuildingImg, BuildingHighlight, UnitDetail, UnitOfBuilding, UnitPhoto, Complex
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
        area = request.GET.get("location", None)
        about = request.GET.get("about", None)
        city = request.GET.get("city", None)
        complex_name = request.GET.get("complex_name", None)
        publish_status = request.GET.get("publish_status", None)

        if complex_name and publish_status is not None:
            complexs = Complex.objects.filter(name__iexact=complex_name)
            for c in complexs:
                c.publish_status = 1
                c.save()
                
        if link and highlight:
            BuildingHighlight.objects.get_or_create(building_link=link, highlight=highlight)
        
        if link and img_link:
            BuildingImg.objects.get_or_create(building_link=link, img_link=img_link)
        
        if link and key and value:
            BuildingDetail.objects.get_or_create(building_link=link, key=key, value=value)

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
                building_area, building_area_created = Area.objects.get_or_create(name=str(area), city=building_city)
                building = Building.objects.create(name=str(name).lower(), building_link=link, status=str(status).lower(), location=str(area).lower(), about=about, area=building_area, city=building_city, publish_status=1)    

            if complex_name is not None:
                complex = Complex.objects.filter(name__iexact=complex_name).first()
                complex.buildings.add(building)

            highlights = BuildingHighlight.objects.filter(building_link=link)
            buildingImgs = BuildingImg.objects.filter(building_link=link)
            details = BuildingDetail.objects.filter(building_link=link)

            for highlight in highlights:
                building.highlight.add(highlight)
                building.save()
            for img in buildingImgs:
                building.img_link.add(img)
                building.save()
            for detail in details:
                building.details.add(detail)
                building.save()
            

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
                    building = Building.objects.filter(Q(name__iexact=building) | Q(building_link=building_link)).first()
                else:
                    building = Building.objects.filter(Q(name__iexact=building_name) | Q(building_link=building_link)).first()
                building.is_ok=1
                building.save()

        if link and key and value :
            UnitDetail.objects.get_or_create(building_link=link, key=key, value=value)
        
        if link and img:
            UnitPhoto.objects.get_or_create(building_link=link, img_link=img)

        if building_name or building_link:
            if price and bath and bed and link:
                building = ProductFilter(building_name, Building.objects.all()).data
                if building:
                    building = Building.objects.filter(Q(name__iexact=building) | Q(building_link=building_link)).first()
                else:
                    building = Building.objects.filter(Q(name__iexact=building_name) | Q(building_link=building_link)).first()

                unit, unit_created = UnitOfBuilding.objects.get_or_create(building_link=link, building_name=building, bed=bed, bath=bath, area=unit_area, desc=description)
                photos = UnitPhoto.objects.filter(building_link=link)
                details = UnitDetail.objects.filter(building_link=link)
            
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
                
        return HttpResponse("ok")
    

class UpdateBuildings(UpdateView):
    def get(self, request):
        link = request.GET.get("link", None)
        status = request.GET.get("status", None)
        name = request.GET.get("name", None)
        location = request.GET.get("location", None)
        about = request.GET.get("about", None)
        source = request.GET.get("source", None)
        
        if link and name and location and about:
            select_buildings = Building.objects.filter(name__iexact=name)
            for select_building in select_buildings:
                select_building.about = about
                select_building.status = status
                select_building.location = location
                select_building.building_link = link
                select_building.created_time = datetime.now()
                select_building.publish_status = 1
                select_building.source = source
                select_building.save()

        return HttpResponse("ok")