# Generated by Django 5.0.4 on 2024-07-17 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('area', '0003_alter_complex_source'),
    ]

    operations = [
        migrations.AlterField(
            model_name='building',
            name='publish_status',
            field=models.BooleanField(default=False),
        ),
    ]
