# Generated by Django 3.1.7 on 2021-11-28 13:44

from django.db import migrations, models
import relic_calculator.models


class Migration(migrations.Migration):

    dependencies = [
        ('relic_calculator', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='relic',
            name='icon',
            field=models.ImageField(null=True, upload_to=relic_calculator.models.rename_to_uuid),
        ),
    ]