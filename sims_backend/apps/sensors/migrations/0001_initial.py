# Generated by Django 5.1.7 on 2025-03-15 11:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sensor_id', models.CharField(max_length=100, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('sensor_type', models.CharField(choices=[('temperature', 'Temperature'), ('moisture', 'Moisture'), ('humidity', 'Humidity'), ('ph', 'pH')], max_length=50)),
                ('location', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='SensorData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.FloatField()),
                ('timestamp', models.DateTimeField()),
                ('sensor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='readings', to='sensors.sensor')),
            ],
            options={
                'ordering': ['-timestamp'],
            },
        ),
    ]
