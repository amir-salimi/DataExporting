# Generated by Django 5.0.4 on 2024-08-05 11:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
            options={
                'verbose_name_plural': 'Cities',
                'db_table': 'cities',
            },
        ),
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('source', models.CharField(max_length=128)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='area.city')),
            ],
            options={
                'verbose_name_plural': 'Areas',
                'db_table': 'areas',
            },
        ),
        migrations.CreateModel(
            name='Community',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('source', models.CharField(max_length=128)),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='area.area')),
                ('city', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='area.city')),
            ],
            options={
                'verbose_name_plural': 'Communities',
                'db_table': 'communities',
            },
        ),
    ]
