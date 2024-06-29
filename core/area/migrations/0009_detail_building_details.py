# Generated by Django 5.0.4 on 2024-06-16 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('area', '0008_alter_building_floor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('description', models.CharField(max_length=256)),
            ],
        ),
        migrations.AddField(
            model_name='building',
            name='details',
            field=models.ManyToManyField(to='area.detail'),
        ),
    ]