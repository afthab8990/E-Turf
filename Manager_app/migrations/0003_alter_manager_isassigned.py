# Generated by Django 5.0 on 2024-07-11 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Manager_app', '0002_manager_isassigned'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manager',
            name='isassigned',
            field=models.IntegerField(default='assigned'),
        ),
    ]
