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