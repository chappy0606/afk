# Generated by Django 3.1.7 on 2021-04-14 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pve_comp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chapterstage',
            name='uploaded_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
