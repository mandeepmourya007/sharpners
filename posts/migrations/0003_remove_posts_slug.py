# Generated by Django 2.1.4 on 2018-12-31 12:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_posts_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posts',
            name='slug',
        ),
    ]
