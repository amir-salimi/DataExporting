# Generated by Django 5.0.4 on 2024-06-16 09:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('export', '0012_alter_product_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 6, 16, 9, 34, 56, 854867)),
        ),
    ]
