# Generated by Django 5.0 on 2024-07-11 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Manager_app', '0003_alter_manager_isassigned'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manager',
            name='isassigned',
            field=models.IntegerField(default=0),
        ),
    ]
