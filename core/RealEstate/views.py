from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.views.generic import CreateView

import ast

from .models import Agent, RealEstate


class HttpResponseOk(HttpResponse):
    status_code = 200


class AgencySet(CreateView):
    def get(self, request):
        name = request.GET.get("name", None)
        agency_photo = request.GET.get("agency_photo", None)
        link = request.GET.get("link", None)
        phone_number = request.GET.get("phone_number", None)
        details = request.GET.get("details", None)
        details = ast.literal_eval(details)
        
        prop_types = None        
        service_areas = None        
        properties = None
        description = None
        brn = None
        arra = None
        ded = None

        for detail in details:
            if "Property Types" in detail:
                prop_types = detail.split(":")
                prop_types = prop_types[1]

            if "Service Areas" in detail:
                service_areas = detail.split(":")
                service_areas = service_areas[1]

            if "Properties" in detail:
                properties = detail.split(":")
                properties = properties[1]

            if "Description" in detail:
                description = detail.split(":")
                description = description[1] 

            if "BRN" in detail:
                brn = detail.split(":")
                brn = brn[1] 

            if "ARRA" in detail:
                arra = detail.split(":")
                arra = arra[1] 
                arra.replace("\n", "")

            if "DED" in detail:
                ded = detail.split(":")
                ded = ded[1] 
                ded.replace("\n", "")   

        
        RealEstate.objects.get_or_create(name=str(name).lower(), photo=agency_photo, link=link, property_types=prop_types, service_areas=service_areas, properties=properties, description=description, brn=brn, arra=arra, ded=ded, phone_number=phone_number)

        return HttpResponseOk()


class AgentSet(CreateView):
    def get(self, request):
        name = request.GET.get("name", None)
        link = request.GET.get("link", None)
        phone_number = request.GET.get("phone_number", None)
        details = request.GET.get("details", None)
        agent_photo = request.GET.get("agent_photo", None)
        agency_link = request.GET.get("agency_link", None)

        languages = None
        specialities = None
        service_areas = None
        properties = None
        description = None
        brn = None
        experience = None
        
        details = ast.literal_eval(details)

        for detail in details:
            if "Language(s)" in detail:
                languages = detail.split(":")
                languages = languages[1]

            if "Specialities" in detail:
                specialities = detail.split(":")
                specialities = specialities[1]

            if "Service Areas" in detail:
                service_areas = detail.split(":")
                service_areas = service_areas[1]

            if "Properties" in detail:
                properties = detail.split(":")
                properties = properties[1]

            if "Description" in detail:
                description = detail.split(":")
                description = description[1] 

            if "BRN" in detail:
                brn = detail.split(":")
                brn = brn[1] 

            if "Experience" in detail:
                experience = detail.split(":")
                experience = experience[1]     
        
        if agency_link is not None:
            real_estate = RealEstate.objects.filter(link=agency_link).first()

        agent, agent_created = Agent.objects.get_or_create(name=str(name).lower(), link=link, photo=agent_photo, languages=languages, specialities=specialities, service_areas=service_areas, properties=properties, description=description, experience=experience, phone_number=phone_number, brn=brn)
        agent.real_estate = real_estate
        agent.save()
        return HttpResponseOk()