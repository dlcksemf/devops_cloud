# Generated by Django 3.2.9 on 2021-12-01 09:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moviereview', '0002_auto_20211201_1821'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='watched_date',
            field=models.DateField(default=datetime.date),
        ),
    ]
