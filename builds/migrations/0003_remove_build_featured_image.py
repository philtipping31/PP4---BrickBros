# Generated by Django 5.0.6 on 2024-06-13 08:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('builds', '0002_build_delete_builds'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='build',
            name='featured_image',
        ),
    ]
