# Generated by Django 3.0.8 on 2021-10-28 02:36

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('passenger', '0027_auto_20211027_0214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='token',
            name='expiry_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 28, 3, 36, 33, 800985, tzinfo=utc)),
        ),
    ]
