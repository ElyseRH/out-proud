# Generated by Django 3.2 on 2022-05-25 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('out_app', '0004_alter_page_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='link',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]
