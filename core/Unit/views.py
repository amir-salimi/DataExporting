from django.http import HttpResponse
from django.db.models import Q
from django.views.generic import CreateView
from django.core.exceptions import ObjectDoesNotExist

from Building.models import Building
from RealEstate.models import Agent, RealEstate

from . models import UnitDetail, UnitOfBuilding, UnitPhoto
from .filter import ProductFilter


class HttpResponseOk(HttpResponse):
    status_code = 200


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
        complex_name = request.GET.get("complex_name", None)
        price = request.GET.get("price", None)
        
        agent_bio_link = request.GET.get("agent_link", None)
        agency_bio_link = request.GET.get("agency_link", None)

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
                building = Building.objects.filter(Q(name=str(building).lower()) | Q(building_link=building_link)).first()
                try:
                    complex = Building.objects.get(name=str(complex_name).lower())
                except ObjectDoesNotExist:
                    complex = None

                agent = Agent.objects.filter(link=agent_bio_link).first()
                agency = RealEstate.objects.filter(link=agency_bio_link).first()
                unit = UnitOfBuilding.objects.create(price=price, building_name=building, agent=agent, agency=agency, building_link=link, bed=bed, bath=bath, area=unit_area, description=description, complex_name=complex)
                
                photos = UnitPhoto.objects.filter(building_link=link)
                details = UnitDetail.objects.filter(building_link=link)
            
                for p in photos:
                    unit.photo.add(p)
                    unit.save()

                for d in details:
                    unit.detail.add(d)
                    unit.save()

        return HttpResponseOk()


