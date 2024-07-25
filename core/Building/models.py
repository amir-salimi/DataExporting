from django.db import models
from django.utils.timezone import now

from area.models import Area, City, Community


class BuildingDetail(models.Model):
    building_link = models.CharField(max_length=128)
    key = models.CharField(max_length=64)
    value = models.CharField(max_length=256)

    class Meta:
        db_table = "building_details"
        verbose_name_plural = 'Building Detials'


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
    must_be_check = 2
    publish = 1
    draft = 0

    PUBLISH_STATUS = (
        (publish, "Publish"),
        (draft, "Draft"),
        (must_be_check, "Must Be Check"),
    )

    city = models.ForeignKey(to=City, on_delete=models.DO_NOTHING, null=True, blank=True)
    area = models.ForeignKey(to=Area, on_delete=models.DO_NOTHING, null=True, blank=True)
    community = models.ForeignKey(to=Community, on_delete=models.DO_NOTHING, null=True, blank=True)
    name = models.CharField(max_length=64)
    source = models.CharField(max_length=128)

    building_link = models.CharField(max_length=128, null=True, blank=True)
    status = models.CharField(max_length=64, null=True, blank=True)
    location = models.CharField(max_length=64, null=True, blank=True)
    about = models.TextField(default=None, null=True, blank=True)
    details = models.ManyToManyField(BuildingDetail, null=True, blank=True)
    img_link = models.ManyToManyField(BuildingImg, null=True, blank=True)
    highlight = models.ManyToManyField(BuildingHighlight, null=True, blank=True)

    publish_status = models.PositiveSmallIntegerField(choices=PUBLISH_STATUS, default=0)
    
    created_time = models.DateTimeField(default=now)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        db_table = "buildings"
        verbose_name_plural = 'Buildings'


class Complex(models.Model):
    must_be_check = 2
    publish = 1
    draft = 0

    PUBLISH_STATUS = (
        (publish, "Publish"),
        (draft, "Draft"),
        (must_be_check, "Must Be Check"),
    )

    name = models.CharField(max_length=64)

    city = models.ForeignKey(to=City, on_delete=models.DO_NOTHING, null=True, blank=True)
    area = models.ForeignKey(to=Area, on_delete=models.DO_NOTHING, null=True, blank=True)
    community = models.ForeignKey(to=Community, on_delete=models.DO_NOTHING, null=True, blank=True)

    buildings = models.ManyToManyField(Building)

    publish_status = models.PositiveSmallIntegerField(choices=PUBLISH_STATUS, default=draft)
    created_time = models.DateTimeField(default=now)

    source = models.CharField(max_length=128, default=None, null=True, blank=True)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        db_table = "complexs"
        verbose_name_plural = 'Complexs'