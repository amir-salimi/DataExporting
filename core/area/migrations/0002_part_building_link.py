# Generated by Django 5.0.4 on 2024-07-01 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('area', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='part',
            name='building_link',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]