# Generated by Django 3.2.7 on 2021-09-25 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkin', '0003_auto_20210925_0253'),
    ]

    operations = [
        migrations.CreateModel(
            name='AvarageTravelTime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_station_id', models.CharField(max_length=256)),
                ('end_station_id', models.CharField(max_length=64)),
            ],
        ),
    ]
