from django.contrib import admin

from .models import City, Area, Community


class SearchCommunity(admin.ModelAdmin):
    search_fields = ["name"]


class SearchArea(admin.ModelAdmin):
    search_fields = ["name"]


class SearchCity(admin.ModelAdmin):
    search_fields = ["name"]


admin.site.register(City, SearchCity)
admin.site.register(Area, SearchArea)
admin.site.register(Community, SearchCommunity)

