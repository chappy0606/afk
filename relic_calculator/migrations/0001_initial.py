# Generated by Django 3.1.7 on 2021-11-25 12:34

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Quality',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Relic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('en_name', models.CharField(max_length=50)),
                ('ja_name', models.CharField(max_length=50)),
                ('cost', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('total_price', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('compornent1', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='compornent1_relic', to='relic_calculator.relic')),
                ('compornent2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='compornent2_relic', to='relic_calculator.relic')),
                ('compornent3', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='compornent3_relic', to='relic_calculator.relic')),
                ('compornent4', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='compornent4_relic', to='relic_calculator.relic')),
                ('quality', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='relic_calculator.quality')),
            ],
        ),
    ]
