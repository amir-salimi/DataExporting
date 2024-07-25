from django.contrib import admin

from .models import UnitDetail, UnitOfBuilding, UnitPhoto

admin.site.register(UnitPhoto)
admin.site.register(UnitDetail)
admin.site.register(UnitOfBuilding)
