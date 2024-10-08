# Generated by Django 5.0 on 2024-07-29 07:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('User_app', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=25)),
                ('cityimage', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='turf',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('turfname', models.CharField(max_length=40)),
                ('capacity', models.IntegerField()),
                ('rate', models.IntegerField()),
                ('turfimage', models.ImageField(upload_to='')),
                ('turflocation', models.CharField(max_length=25)),
                ('isbooked', models.BooleanField(default=False)),
                ('managerof', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(default=0)),
                ('bslot', models.CharField(max_length=100)),
                ('booked', models.BooleanField(default=False)),
                ('buser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User_app.user')),
                ('bturf', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin_app.turf')),
            ],
        ),
    ]
