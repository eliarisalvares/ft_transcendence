# Generated by Django 5.0.1 on 2024-05-01 02:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '009_auto_20240224_2308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='twofactor',
            name='expiration',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 1, 4, 12, 37, 307494, tzinfo=datetime.timezone.utc)),
        ),
    ]