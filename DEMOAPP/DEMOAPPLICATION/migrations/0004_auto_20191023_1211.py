# Generated by Django 2.2.6 on 2019-10-23 11:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DEMOAPPLICATION', '0003_auto_20191023_1208'),
    ]

    operations = [
        migrations.AddField(
            model_name='guest',
            name='guest_phonenumber',
            field=models.CharField(default=234543453, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='guest',
            name='guest_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 23, 12, 11, 30, 392320), verbose_name='Date login'),
        ),
    ]
