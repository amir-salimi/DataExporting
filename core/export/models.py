from django.db import models

from django.core.validators import MinValueValidator

from datetime import datetime



class ProductPlanMap(models.Model):
    link = models.CharField(max_length=128, null=True, blank=True)
    plan_map = models.CharField(max_length=256)

class Category(models.Model):
    category = models.CharField(unique=True, max_length=64, null=True, blank=True)

class Status(models.Model):
    status = models.CharField(unique=True, max_length=32, null=True, blank=True)

class AnswerAndQuestion(models.Model):
    link = models.CharField(max_length=128, null=True, blank=True)
    question = models.CharField(max_length=256)
    answer = models.TextField()

class ProductPhoto(models.Model):
    link = models.CharField(max_length=128, null=True, blank=True)
    image = models.CharField(max_length=256)

class About(models.Model):
    link = models.CharField(max_length=128, null=True, blank=True)
    about = models.TextField()

class Product(models.Model):
    name = models.CharField(max_length=256)
    location = models.CharField(max_length=128, null=True, blank=True)
    developer = models.CharField(max_length=128, null=True, blank=True)
    link = models.CharField(max_length=128, null=True, blank=True)
    category = models.ForeignKey(to=Category, on_delete=models.DO_NOTHING, null=True, blank=True)
    price = models.FloatField(validators=[MinValueValidator(1000)], null=True, blank=True)
    per_meter_price = models.PositiveIntegerField(validators=[MinValueValidator(0)], null=True, blank=True)
    area = models.FloatField(validators=[MinValueValidator(10)], null=True, blank=True)
    payment_plan = models.CharField(max_length=64, null=True, blank=True)
    status = models.ForeignKey(to=Status, on_delete=models.DO_NOTHING, null=True, blank=True)
    bed_room = models.CharField(max_length=16, null=True, blank=True)
    handover = models.CharField(max_length=32, null=True, blank=True)
    frequntly_question = models.ManyToManyField(AnswerAndQuestion, null=True, blank=True)
    viwes = models.PositiveIntegerField(null=True, blank=True)
    city = models.CharField(max_length=64, null=True, blank=True)
    photo = models.ManyToManyField(ProductPhoto, null=True, blank=True)
    plan_map = models.ManyToManyField(ProductPlanMap, null=True, blank=True)
    about = models.ManyToManyField(About, null=True, blank=True)
    approximate_location = models.TextField(null=True, blank=True)
    development = models.CharField(max_length=128, null=True, blank=True)
    developer_project_number = models.PositiveIntegerField(null=True, blank=True)
    created_at = models.DateTimeField(default=datetime.now(), blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    type = models.CharField(max_length=64, null=True, blank=True)
    finish = models.CharField(max_length=64, null=True, blank=True)
    
