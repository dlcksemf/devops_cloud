# Generated by Django 3.2.9 on 2021-12-08 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='music',
            name='released_date',
            field=models.DateField(),
        ),
    ]
