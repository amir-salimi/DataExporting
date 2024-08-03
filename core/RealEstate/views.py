from django.shortcuts import render
from rest_framework.viewsets import generics


from .serializers import RealEstateModelSerializer, AgentModelSerializer
from .models import Agent, Agency


class AgencySet(generics.CreateAPIView):
    queryset = Agency.objects.all()
    serializer_class = RealEstateModelSerializer


class AgentSet(generics.CreateAPIView):
    queryset = Agent.objects.all()
    serializer_class = AgentModelSerializer


