from django.shortcuts import render

from django.views.generic import DetailView


class CityProperties(DetailView):
    def get(self, request):
        print(request.GET.get("city"))