# Generated by Django 3.0.8 on 2021-10-25 06:26

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('passenger', '0008_auto_20211025_0626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='token',
            name='expiry_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 25, 7, 26, 21, 512523, tzinfo=utc)),
        ),
    ]