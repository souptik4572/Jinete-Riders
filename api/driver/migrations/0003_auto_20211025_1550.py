# Generated by Django 3.0.8 on 2021-10-25 15:50

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('driver', '0002_auto_20211025_1442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='token',
            name='expiry_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 25, 16, 50, 13, 213516, tzinfo=utc)),
        ),
    ]
