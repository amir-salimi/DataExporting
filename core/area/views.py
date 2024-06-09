from django.shortcuts import render

from django.http import HttpResponse

from django.views.generic import DetailView


from .models import City, Area, Community, Part


class CityProperties(DetailView):
    def get(self, request):

        city = request.GET.get("city", None)
        area = request.GET.get("area", None) 
        community = request.GET.get("community", None) 
        part = request.GET.get("part", None) 

        city, city_created = City.objects.get_or_create(city=city)

        if area is not None:
            area, area_created = Area.objects.get_or_create(area=area, city=city)
            if community is not None:
                community, community_created = Community.objects.get_or_create(area=area, community=community)
                if part is not None:
                    part, part_created = Part.objects.get_or_create(community=community, part=part)

        print(city)
        print(area)
        return HttpResponse("ok")