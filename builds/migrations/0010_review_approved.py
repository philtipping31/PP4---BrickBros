# Generated by Django 5.0.6 on 2024-06-26 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('builds', '0009_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='approved',
            field=models.BooleanField(default=False),
        ),
    ]