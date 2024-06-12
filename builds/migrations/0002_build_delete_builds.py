# Generated by Django 5.0.6 on 2024-06-12 15:04

import cloudinary.models
import django.db.models.deletion
import django_resized.forms
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('builds', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Build',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('build_title', models.CharField(max_length=250)),
                ('featured_image', cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image')),
                ('slug', models.SlugField(max_length=250, unique=True)),
                ('image', django_resized.forms.ResizedImageField(crop=None, force_format='WEBP', keep_meta=True, quality=75, scale=None, size=[400, None], upload_to='builds/')),
                ('image_alt', models.CharField(max_length=100)),
                ('set_number', models.IntegerField()),
                ('build_time', models.DurationField()),
                ('build_type', models.CharField(choices=[('designed_by_lego', 'Designed By Lego'), ('selfmade', 'Self Made')], default='designed_by_lego', max_length=50)),
                ('difficulty_rating', models.CharField(choices=[('easy', 'Easy'), ('medium', 'Medium'), ('hard', 'Hard'), ('expert', 'Expert')], default='easy', max_length=10)),
                ('content', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='build_owner', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
        migrations.DeleteModel(
            name='Builds',
        ),
    ]
