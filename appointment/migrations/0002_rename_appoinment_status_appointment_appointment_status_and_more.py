# Generated by Django 4.2.11 on 2024-04-26 10:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appointment',
            old_name='appoinment_status',
            new_name='appointment_status',
        ),
        migrations.RenameField(
            model_name='appointment',
            old_name='appoinment_types',
            new_name='appointment_types',
        ),
    ]