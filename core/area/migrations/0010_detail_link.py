# Generated by Django 5.0.4 on 2024-06-16 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('area', '0009_detail_building_details'),
    ]

    operations = [
        migrations.AddField(
            model_name='detail',
            name='link',
            field=models.CharField(default='', max_length=128),
            preserve_default=False,
        ),
    ]
