from django.db import models
from django.utils.timezone import now

from area.models import City, Area


class RealEstate(models.Model):
    name = models.CharField(max_length=64)
    photo = models.CharField(max_length=128, null=True, blank=True)
    link = models.CharField(max_length=128)
    
    property_types = models.CharField(max_length=128)
    service_areas = models.CharField(max_length=256)
    properties = models.CharField(max_length=64)
    description = models.TextField()
    brn = models.CharField(max_length=9, verbose_name="BRN", null=True, blank=True)
    arra = models.CharField(max_length=9, verbose_name="ARRA", null=True, blank=True)
    ded = models.CharField(max_length=9, verbose_name="DED", null=True, blank=True)

    phone_number = models.CharField(max_length=18)
    created_at = models.DateTimeField(default=now)

    class Meta:
        db_table = "real_estates"
        verbose_name_plural = 'Real Estate'

    def __str__(self) -> str:
        return self.name


class Agent(models.Model):
    name = models.CharField(max_length=64)
    link = models.CharField(max_length=128)
    photo = models.CharField(max_length=128, null=True, blank=True)
    languages = models.CharField(max_length=64)
    specialities = models.CharField(max_length=128)
    service_areas = models.CharField(max_length=256)
    properties = models.CharField(max_length=64)
    description = models.TextField()
    experience = models.CharField(max_length=64, null=True, blank=True)
    phone_number = models.CharField(max_length=18)
    brn = models.CharField(max_length=9, verbose_name="BRN", null=True, blank=True)
    created_at = models.DateTimeField(default=now)

    real_estate = models.ForeignKey(to=RealEstate, on_delete=models.DO_NOTHING, null=True, blank=True)

    class Meta:
        db_table = "agents"
        verbose_name_plural = 'Agents'

    def __str__(self) -> str:
        return self.name
