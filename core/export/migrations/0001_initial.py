# Generated by Django 5.0.4 on 2024-05-10 15:06

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(blank=True, max_length=128, null=True)),
                ('about', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='AnswerAndQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(blank=True, max_length=128, null=True)),
                ('question', models.CharField(max_length=256)),
                ('answer', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(blank=True, max_length=64, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(blank=True, max_length=128, null=True)),
                ('image', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='ProductPlanMap',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(blank=True, max_length=128, null=True)),
                ('plan_map', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(blank=True, max_length=32, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('location', models.CharField(blank=True, max_length=128, null=True)),
                ('developer', models.CharField(blank=True, max_length=128, null=True)),
                ('link', models.CharField(blank=True, max_length=128, null=True)),
                ('price', models.PositiveBigIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1000)])),
                ('per_meter_price', models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0)])),
                ('area', models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(10)])),
                ('payment_plan', models.CharField(blank=True, max_length=64, null=True)),
                ('bed_room', models.CharField(blank=True, max_length=16, null=True)),
                ('handover', models.CharField(blank=True, max_length=32, null=True)),
                ('viwes', models.PositiveIntegerField(blank=True, null=True)),
                ('city', models.CharField(blank=True, max_length=64, null=True)),
                ('approximate_location', models.TextField(blank=True, null=True)),
                ('about', models.ManyToManyField(blank=True, null=True, to='export.about')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='export.category')),
                ('frequntly_question', models.ManyToManyField(blank=True, null=True, to='export.answerandquestion')),
                ('photo', models.ManyToManyField(blank=True, null=True, to='export.productphoto')),
                ('plan_map', models.ManyToManyField(blank=True, null=True, to='export.productplanmap')),
                ('status', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='export.status')),
            ],
        ),
    ]
