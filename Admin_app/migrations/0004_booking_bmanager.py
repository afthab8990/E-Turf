# Generated by Django 5.0 on 2024-09-19 06:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin_app', '0003_alter_booking_booked'),
        ('Manager_app', '0005_manager_isapproved'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='bmanager',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Manager_app.manager'),
            preserve_default=False,
        ),
    ]
