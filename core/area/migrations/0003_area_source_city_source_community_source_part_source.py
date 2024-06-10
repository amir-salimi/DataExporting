# Generated by Django 5.0.4 on 2024-06-10 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('area', '0002_part'),
    ]

    operations = [
        migrations.AddField(
            model_name='area',
            name='source',
            field=models.CharField(default='', max_length=128),
        ),
        migrations.AddField(
            model_name='city',
            name='source',
            field=models.CharField(default='', max_length=128),
        ),
        migrations.AddField(
            model_name='community',
            name='source',
            field=models.CharField(default='', max_length=128),
        ),
        migrations.AddField(
            model_name='part',
            name='source',
            field=models.CharField(default='', max_length=128),
        ),
    ]