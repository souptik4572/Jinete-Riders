# Generated by Django 3.0.8 on 2021-10-25 14:41

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('email', models.CharField(max_length=320, unique=True)),
                ('phone', models.CharField(max_length=15)),
                ('password', models.CharField(max_length=128)),
                ('city', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=60)),
                ('profile_image', models.CharField(blank=True, max_length=256, null=True)),
                ('rating', models.FloatField(default=3)),
                ('car_name', models.CharField(max_length=50)),
                ('car_number', models.CharField(max_length=30)),
                ('car_image', models.CharField(max_length=256)),
                ('driving_license_no', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Token',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=100)),
                ('expiry_time', models.DateTimeField(default=datetime.datetime(2021, 10, 25, 15, 41, 52, 583629, tzinfo=utc))),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='driver.Driver')),
            ],
        ),
    ]
