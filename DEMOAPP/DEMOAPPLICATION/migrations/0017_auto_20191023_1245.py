# Generated by Django 2.2.6 on 2019-10-23 11:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DEMOAPPLICATION', '0016_auto_20191023_1245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guest',
            name='guest_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 23, 12, 45, 21, 344893), verbose_name='Date login'),
        ),
    ]
