# Generated by Django 3.0.8 on 2021-10-28 13:59

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('driver', '0019_auto_20211028_1230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='token',
            name='expiry_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 28, 14, 59, 29, 895339, tzinfo=utc)),
        ),
    ]
