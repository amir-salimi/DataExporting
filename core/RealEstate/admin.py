from django.contrib import admin

from .models import RealEstate, Agent, PropertyType


admin.site.register(RealEstate)
admin.site.register(Agent)
admin.site.register(PropertyType)