# Generated by Django 5.0.4 on 2024-06-19 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('area', '0012_buildingimg_rename_area_building_location_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='BuildingStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(max_length=128)),
                ('status', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Highlight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(max_length=128)),
                ('highlight', models.CharField(max_length=64)),
            ],
        ),
        migrations.AddField(
            model_name='building',
            name='highlight',
            field=models.ManyToManyField(to='area.highlight'),
        ),
    ]