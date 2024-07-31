from django.db import models
from django.utils.timezone import now

from Building.models import Building, Complex
from RealEstate.models import Agent, RealEstate


class UnitPhoto(models.Model):
    building_link = models.CharField(max_length=128)
    img_link = models.CharField(max_length=128)
    class Meta:
        db_table = "unit_photos"
        verbose_name_plural = 'Unit Photos'


class UnitDetail(models.Model):
    building_link = models.CharField(max_length=128)
    key = models.CharField(max_length=64)
    value = models.CharField(max_length=256)

    class Meta:
        db_table = "unit_detials"
        verbose_name_plural = 'Unit Details'


class UnitOfBuilding(models.Model):
    building_name = models.ForeignKey(Building, on_delete=models.DO_NOTHING)
    bed = models.CharField(max_length=32)
    bath = models.CharField(max_length=32)
    area = models.CharField(max_length=32)
    description = models.TextField()
    building_link = models.CharField(max_length=128)
    photo = models.ManyToManyField(UnitPhoto, null=True, blank=True)
    detail = models.ManyToManyField(UnitDetail, null=True, blank=True)
    complex_name = models.ForeignKey(to=Complex, on_delete=models.DO_NOTHING, null=True, blank=True)
    created_time = models.DateTimeField(default=now)
    price = models.CharField(max_length=32)
    agent = models.ForeignKey(to=Agent, on_delete=models.DO_NOTHING, null=True, blank=True)
    agency = models.ForeignKey(to=RealEstate, on_delete=models.DO_NOTHING, null=True, blank=True)

    class Meta:
        db_table = "unit_of_buildings"
        verbose_name_plural = 'Unit Of Buildings'

        