# Generated by Django 5.0.4 on 2024-07-25 08:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('area', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='realestate',
            name='property_types',
        ),
        migrations.RemoveField(
            model_name='realestate',
            name='service_areas',
        ),
        migrations.RemoveField(
            model_name='realestate',
            name='service_cities',
        ),
        migrations.DeleteModel(
            name='Agent',
        ),
        migrations.DeleteModel(
            name='PropertyType',
        ),
        migrations.DeleteModel(
            name='RealEstate',
        ),
    ]