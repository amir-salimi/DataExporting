# Generated by Django 5.0.4 on 2024-08-04 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Building', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buildingimg',
            name='building_link',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='buildingimg',
            name='img_link',
            field=models.CharField(max_length=320),
        ),
    ]