# Generated by Django 3.0.7 on 2020-06-23 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catwiki', '0003_remove_home_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='home',
            name='slug',
            field=models.SlugField(default='', max_length=40),
        ),
    ]