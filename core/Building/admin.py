from django.contrib import admin

from .models import Building, BuildingDetail, BuildingImg, BuildingHighlight, Complex

class SearchBuildings(admin.ModelAdmin):
    search_fields = ["name"]


admin.site.register(Building, SearchBuildings)
admin.site.register(BuildingDetail)
admin.site.register(BuildingImg)
admin.site.register(BuildingHighlight)
admin.site.register(Complex)