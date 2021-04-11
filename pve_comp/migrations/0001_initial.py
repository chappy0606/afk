# Generated by Django 3.1.7 on 2021-04-11 10:53

from django.db import migrations, models
import django.utils.timezone
import pve_comp.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ChapterStage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chapter', models.CharField(max_length=4)),
                ('stage', models.CharField(max_length=4)),
                ('uploaded_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('uploaded_image', models.ImageField(upload_to=pve_comp.models.rename_to_uuid)),
            ],
        ),
    ]
