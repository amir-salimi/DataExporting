from django.db import models
from django.utils.timezone import now
from django.core.validators import MinValueValidator


class City(models.Model):
    name = models.CharField(max_length=64)

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
        return str(self.name)  
    
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
    


