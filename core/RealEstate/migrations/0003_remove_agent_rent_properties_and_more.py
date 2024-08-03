# Generated by Django 5.0.4 on 2024-07-29 08:44

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RealEstate', '0002_agent_link_alter_agent_phone_number_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='agent',
            name='rent_properties',
        ),
        migrations.RemoveField(
            model_name='agent',
            name='sale_properties',
        ),
        migrations.RemoveField(
            model_name='agent',
            name='service_cities',
        ),
        migrations.RemoveField(
            model_name='realestate',
            name='rent_properties',
        ),
        migrations.RemoveField(
            model_name='realestate',
            name='sale_properties',
        ),
        migrations.RemoveField(
            model_name='realestate',
            name='service_cities',
        ),
        migrations.AddField(
            model_name='agent',
            name='brn',
            field=models.CharField(default='', max_length=9, verbose_name='BRN'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='agent',
            name='properties',
            field=models.CharField(default='', max_length=64),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='realestate',
            name='brn',
            field=models.CharField(default='', max_length=9, verbose_name='BRN'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='realestate',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='realestate',
            name='link',
            field=models.CharField(default='', max_length=128),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='realestate',
            name='properties',
            field=models.CharField(default='', max_length=64),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='agent',
            name='experience',
            field=models.CharField(max_length=64),
        ),
        migrations.RemoveField(
            model_name='agent',
            name='service_areas',
        ),
        migrations.RemoveField(
            model_name='realestate',
            name='property_types',
        ),
        migrations.RemoveField(
            model_name='realestate',
            name='service_areas',
        ),
        migrations.AddField(
            model_name='agent',
            name='service_areas',
            field=models.CharField(default='', max_length=256),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='realestate',
            name='property_types',
            field=models.CharField(default='', max_length=128),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='realestate',
            name='service_areas',
            field=models.CharField(default='', max_length=256),
            preserve_default=False,
        ),
    ]