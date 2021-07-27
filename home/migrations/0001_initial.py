# Generated by Django 3.1.7 on 2021-06-26 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='homework',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='homework title')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('desc', models.TextField(verbose_name='Description')),
                ('img', models.ImageField(upload_to='')),
                ('slug', models.SlugField(unique=True)),
                ('img1', models.ImageField(null=True, upload_to='', verbose_name='exercice')),
                ('img2', models.ImageField(null=True, upload_to='', verbose_name='solution')),
            ],
            options={
                'verbose_name': 'homework title',
            },
        ),
    ]