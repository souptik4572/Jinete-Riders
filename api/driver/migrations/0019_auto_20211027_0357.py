# Generated by Django 3.0.8 on 2021-10-27 03:57

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('driver', '0018_auto_20211027_0354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='id',
            field=models.TextField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='token',
            name='expiry_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 27, 4, 57, 28, 755949, tzinfo=utc)),
        ),
    ]
