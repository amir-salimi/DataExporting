from django.db import models

class City(models.Model):
    city = models.CharField(max_length=64)

    def __str__(self) -> str:
        return self.city
    

class Area(models.Model):
    city = models.ForeignKey(to=City, on_delete=models.DO_NOTHING)
    area = models.CharField(max_length=64)

    def __str__(self) -> str:
        return self.area


class Community(models.Model):
    area = models.ForeignKey(to=Area, on_delete=models.DO_NOTHING)
    community = models.CharField(max_length=64)

    def __str__(self) -> str:
        return self.community

class Part(models.Model):
    community = models.ForeignKey(to=Community, on_delete=models.DO_NOTHING)
    part = models.CharField(max_length=64)

    def __str__(self) -> str:
        return self.part