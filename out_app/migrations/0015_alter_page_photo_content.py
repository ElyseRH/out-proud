# Generated by Django 3.2 on 2022-04-17 11:33

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('out_app', '0014_auto_20220417_1121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='photo_content',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255),
        ),
    ]
