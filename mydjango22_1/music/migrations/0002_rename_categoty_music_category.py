# Generated by Django 3.2.10 on 2021-12-14 05:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='music',
            old_name='categoty',
            new_name='category',
        ),
    ]
