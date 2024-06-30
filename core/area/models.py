from django.db import models
from django.core.validators import MinValueValidator


class City(models.Model):
    name = models.CharField(max_length=64)
    source = models.CharField(max_length=128)

    def __str__(self) -> str:
        return self.name

    class Meta:
        db_table = "cities"
        verbose_name_plural = 'Cities'
    


class Area(models.Model):
    city = models.ForeignKey(to=City, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=64)
    source = models.CharField(max_length=128)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        db_table = "areas"
        verbose_name_plural = 'Areas'


class Community(models.Model):
    city = models.ForeignKey(to=City, on_delete=models.DO_NOTHING, null=True, blank=True)
    area = models.ForeignKey(to=Area, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=64)
    source = models.CharField(max_length=128)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        db_table = "communities"
        verbose_name_plural = 'Communities'

class Part(models.Model):
    city = models.ForeignKey(to=City, on_delete=models.DO_NOTHING, null=True, blank=True)
    area = models.ForeignKey(to=Area, on_delete=models.DO_NOTHING, null=True, blank=True)
    community = models.ForeignKey(to=Community, on_delete=models.DO_NOTHING, null=True, blank=True)
    name = models.CharField(max_length=64)
    source = models.CharField(max_length=128)
    

#----------------------------------------------------------------



class BuildingDetail(models.Model):
    building_link = models.CharField(max_length=128)
    key = models.CharField(max_length=64)
    value = models.CharField(max_length=256)

    class Meta:
        db_table = "building_details"
        verbose_name_plural = 'Detials'


class BuildingImg(models.Model):
    building_link = models.CharField(max_length=128)
    img_link = models.CharField(max_length=128)

    class Meta:
        db_table = "building_images"
        verbose_name_plural = 'Building Images'


class BuildingHighlight(models.Model):
    building_link = models.CharField(max_length=128)
    highlight = models.CharField(max_length=64)

    class Meta:
        db_table = "building_highlights"
        verbose_name_plural = 'Building Highlights'


class Building(models.Model):
    name = models.CharField(max_length=64)
    building_link = models.CharField(max_length=128)
    status = models.CharField(max_length=64)
    location = models.CharField(max_length=64)
    about = models.TextField()
    details = models.ManyToManyField(BuildingDetail)
    img_link = models.ManyToManyField(BuildingImg)
    highlight = models.ManyToManyField(BuildingHighlight)
    
    is_ok = models.SmallIntegerField(default=0)

    city = models.CharField(max_length=64, null=True, blank=True)
    area = models.CharField(max_length=64, null=True, blank=True)
    community = models.CharField(max_length=64, null=True, blank=True)
    part = models.CharField(max_length=64, null=True, blank=True)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        db_table = "buildings"
        verbose_name_plural = 'Buildings'





#---------------------------------------------------------------------------------------------------------


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
    building_name = models.ForeignKey(Building, on_delete=models.CASCADE)
    bed = models.CharField(max_length=32)
    bath = models.CharField(max_length=32)
    area = models.CharField(max_length=32)
    desc = models.TextField()
    link = models.CharField(max_length=128)
    photo = models.ManyToManyField(UnitPhoto, null=True, blank=True)
    detail = models.ManyToManyField(UnitDetail, null=True, blank=True)

    class Meta:
        db_table = "unit_of_buildings"
        verbose_name_plural = 'Unit Of Buildings'