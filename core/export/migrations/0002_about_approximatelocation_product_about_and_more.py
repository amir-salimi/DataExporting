# Generated by Django 5.0.4 on 2024-05-09 19:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('export', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='ApproximateLocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('located', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='about',
            field=models.ManyToManyField(blank=True, null=True, to='export.about'),
        ),
        migrations.AddField(
            model_name='product',
            name='approximate_location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='export.approximatelocation'),
        ),
    ]
