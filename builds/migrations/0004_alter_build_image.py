# Generated by Django 5.0.6 on 2024-06-13 14:44

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('builds', '0003_remove_build_featured_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='build',
            name='image',
            field=cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image'),
        ),
    ]
