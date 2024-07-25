from django.db import models
from django.utils.timezone import now

from area.models import City, Area

class PropertyType(models.Model):
    name = models.CharField(max_length=32)
    
    class Meta:
        db_table = "property_type"
        verbose_name_plural = 'Property Type'
    
    def __str__(self) -> str:
        return self.name


class RealEstate(models.Model):
    name = models.CharField(max_length=64)
    photo = models.CharField(max_length=128)
    property_types = models.ManyToManyField(PropertyType)
    service_cities = models.ManyToManyField(City)
    service_areas = models.ManyToManyField(Area)
    sale_properties = models.PositiveSmallIntegerField()
    rent_properties = models.PositiveSmallIntegerField()
    description = models.TextField()

    class Meta:
        db_table = "real_estates"
        verbose_name_plural = 'Real Estate'

    def __str__(self) -> str:
        return self.name


class Agent(models.Model):
    name = models.CharField(max_length=64)
    photo = models.CharField(max_length=128)
    languages = models.CharField(max_length=64)
    specialities = models.CharField(max_length=128)
    service_cities = models.ManyToManyField(City)
    service_areas = models.ManyToManyField(Area)
    sale_properties = models.PositiveSmallIntegerField()
    rent_properties = models.PositiveSmallIntegerField()
    description = models.TextField()
    experience = models.PositiveSmallIntegerField() # years
    phone_number = models.CharField(max_length=15)
    created_at = models.DateTimeField(default=now)

    real_estate = models.ForeignKey(to=RealEstate, on_delete=models.DO_NOTHING)

    class Meta:
        db_table = "agents"
        verbose_name_plural = 'Agents'

    def __str__(self) -> str:
        return self.name
