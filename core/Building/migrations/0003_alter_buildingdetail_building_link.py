# Generated by Django 5.0.4 on 2024-08-05 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Building', '0002_alter_buildinghighlight_highlight'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buildingdetail',
            name='building_link',
            field=models.CharField(max_length=255),
        ),
    ]