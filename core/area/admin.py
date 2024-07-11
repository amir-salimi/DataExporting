from django.contrib import admin

from .models import City, Area, Community, Building, BuildingDetail, BuildingImg, BuildingHighlight, UnitDetail, UnitOfBuilding, UnitPhoto


class SearchCommunity(admin.ModelAdmin):
    search_fields = ["name"]


class SearchBuildings(admin.ModelAdmin):
    search_fields = ["name"]

class SearchArea(admin.ModelAdmin):
    search_fields = ["name"]


class SearchCity(admin.ModelAdmin):
    search_fields = ["name"]


admin.site.register(City, SearchCity)
admin.site.register(Area, SearchArea)
admin.site.register(Community, SearchCommunity)
admin.site.register(Building, SearchBuildings)
admin.site.register(BuildingDetail)
admin.site.register(BuildingImg)
admin.site.register(BuildingHighlight)
admin.site.register(UnitPhoto)
admin.site.register(UnitDetail)
admin.site.register(UnitOfBuilding)