# Generated by Django 3.0.7 on 2020-06-22 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catwiki', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='home',
            name='slug',
            field=models.SlugField(blank=True, max_length=200, null=True),
        ),
    ]
