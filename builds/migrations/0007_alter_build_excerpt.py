# Generated by Django 5.0.6 on 2024-06-14 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('builds', '0006_alter_build_excerpt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='build',
            name='excerpt',
            field=models.CharField(max_length=100),
        ),
    ]