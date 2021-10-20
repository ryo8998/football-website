# Generated by Django 3.2.8 on 2021-10-18 14:38

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Players',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('thumbnail', models.CharField(max_length=250)),
                ('pic', models.CharField(max_length=250)),
                ('player_team', models.CharField(max_length=100)),
                ('age', models.IntegerField(validators=[django.core.validators.MinValueValidator(15)])),
                ('height_M', models.FloatField(validators=[django.core.validators.MinValueValidator(0)])),
                ('weight_Kg', models.FloatField(validators=[django.core.validators.MinValueValidator(0)])),
            ],
        ),
    ]
