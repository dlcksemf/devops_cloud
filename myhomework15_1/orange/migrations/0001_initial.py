# Generated by Django 3.2.9 on 2021-12-04 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('artist', models.CharField(max_length=30)),
                ('album', models.CharField(max_length=30)),
                ('genre', models.CharField(max_length=20)),
                ('released_date', models.DateTimeField()),
                ('description', models.TextField()),
                ('album_cover', models.ImageField(null=True, upload_to='')),
                ('korean_music', models.BooleanField(null=True)),
            ],
        ),
    ]
