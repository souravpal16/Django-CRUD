# Generated by Django 3.1.4 on 2020-12-05 20:59

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PizzaApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pizzamodel',
            name='toppings',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=15), size=None),
        ),
    ]
