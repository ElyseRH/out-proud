# Generated by Django 3.2 on 2022-04-16 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('out_app', '0015_alter_page_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='slug',
            field=models.SlugField(primary_key=True, serialize=False, unique=True, verbose_name='Page code'),
        ),
    ]