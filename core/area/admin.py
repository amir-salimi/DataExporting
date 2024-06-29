from django.contrib import admin

from .models import City, Area, Community, Part, Building, Detail, BuildingImg, Highlight, UnitDetail, UnitOfBuilding, UnitPhoto

class SearchPart(admin.ModelAdmin):
    search_fields = ["part"]


class SearchCommunity(admin.ModelAdmin):
    search_fields = ["community"]


class SearchBuildings(admin.ModelAdmin):
    search_fields = ["name", "community"]

class SearchArea(admin.ModelAdmin):
    search_fields = ["area"]


class SearchCity(admin.ModelAdmin):
    search_fields = ["city"]

admin.site.register(City, SearchCity)
admin.site.register(Area, SearchArea)
admin.site.register(Community, SearchCommunity)
admin.site.register(Part, SearchPart)
admin.site.register(Detail)
admin.site.register(Building, SearchBuildings)
admin.site.register(BuildingImg)
admin.site.register(Highlight)
admin.site.register(UnitPhoto)
admin.site.register(UnitDetail)
admin.site.register(UnitOfBuilding)