# Generated by Django 5.0.4 on 2024-06-22 12:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('area', '0015_unitdetail_unitphoto_building_area_building_city_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='unitofbuilding',
            old_name='building_name',
            new_name='name',
        ),
    ]
