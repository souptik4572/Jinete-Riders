# Generated by Django 3.0.8 on 2021-10-29 17:30

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('driver', '0021_auto_20211028_1515'),
    ]

    operations = [
        migrations.AlterField(
            model_name='token',
            name='expiry_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 29, 18, 30, 33, 971874, tzinfo=utc)),
        ),
    ]
