# Generated by Django 3.2.10 on 2021-12-15 12:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=20, unique=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(db_index=True, max_length=200)),
                ('content', models.TextField()),
                ('photo', models.ImageField(upload_to='blog/post/%Y/%m/%d')),
                ('status', models.CharField(choices=[('D', 'Draft'), ('P', 'Publish')], db_index=True, default='D', max_length=1)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.category')),
                ('tag_set', models.ManyToManyField(blank=True, to='blog.Tag')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('message', models.TextField()),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.post')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]
