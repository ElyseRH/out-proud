# Generated by Django 3.2 on 2022-04-15 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('out_app', '0011_auto_20220413_1138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='slug',
            field=models.SlugField(max_length=12, primary_key=True, serialize=False, unique=True),
        ),
    ]
