from django.db import models
from django.core.validators import MinValueValidator


class City(models.Model):
    city = models.CharField(max_length=64)
    source = models.CharField(max_length=128)

    def __str__(self) -> str:
        return self.city
    

class Area(models.Model):
    city = models.ForeignKey(to=City, on_delete=models.DO_NOTHING)
    area = models.CharField(max_length=64)
    source = models.CharField(max_length=128)

    def __str__(self) -> str:
        return self.area


class Community(models.Model):
    area = models.ForeignKey(to=Area, on_delete=models.DO_NOTHING)
    community = models.CharField(max_length=64)
    source = models.CharField(max_length=128)

    def __str__(self) -> str:
        return self.community

class Part(models.Model):
    community = models.ForeignKey(to=Community, on_delete=models.DO_NOTHING)
    part = models.CharField(max_length=64)
    source = models.CharField(max_length=128)

    def __str__(self) -> str:
        return self.part


class Detail(models.Model):
    link = models.CharField(max_length=128)
    key = models.CharField(max_length=64)
    value = models.CharField(max_length=256)


class BuildingImg(models.Model):
    link = models.CharField(max_length=128)
    img_link = models.CharField(max_length=128)


class BuildingStatus(models.Model):
    link = models.CharField(max_length=128)
    status = models.CharField(max_length=64)


class Highlight(models.Model):
    link = models.CharField(max_length=128)
    highlight = models.CharField(max_length=64)


class Building(models.Model):
    name = models.CharField(max_length=64)
    link = models.CharField(max_length=128)
    status = models.CharField(max_length=64)
    location = models.CharField(max_length=64)
    about = models.TextField()
    details = models.ManyToManyField(Detail)
    img_link = models.ManyToManyField(BuildingImg)
    highlight = models.ManyToManyField(Highlight)
    
    is_ok = models.SmallIntegerField(default=0)

    city = models.CharField(max_length=64, null=True, blank=True)
    area = models.CharField(max_length=64, null=True, blank=True)
    community = models.CharField(max_length=64, null=True, blank=True)
    part = models.CharField(max_length=64, null=True, blank=True)

    def __str__(self) -> str:
        return self.name
    
    # class Meta:
    #     ordering = ('name',)


class UnitPhoto(models.Model):
    link = models.CharField(max_length=128)
    img_link = models.CharField(max_length=128)


class UnitDetail(models.Model):
    link = models.CharField(max_length=128)
    key = models.CharField(max_length=64)
    value = models.CharField(max_length=256)


class UnitOfBuilding(models.Model):
    building_name = models.ForeignKey(Building, on_delete=models.CASCADE)
    bed = models.CharField(max_length=32)
    bath = models.CharField(max_length=32)
    area = models.CharField(max_length=32)
    desc = models.TextField()
    link = models.CharField(max_length=128)
    photo = models.ManyToManyField(UnitPhoto, null=True, blank=True)
    detail = models.ManyToManyField(UnitDetail, null=True, blank=True)

    # class Meta:
    #     ordering = ('building_name',)