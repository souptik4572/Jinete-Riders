# Generated by Django 3.0.8 on 2021-10-25 06:25

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('passenger', '0004_auto_20211025_0548'),
    ]

    operations = [
        migrations.AlterField(
            model_name='token',
            name='expiry_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 25, 7, 25, 39, 963133, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='token',
            name='token',
            field=models.CharField(max_length=100),
        ),
    ]
