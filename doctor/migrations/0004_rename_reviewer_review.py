# Generated by Django 4.2.11 on 2024-04-26 05:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0002_alter_patient_user'),
        ('doctor', '0003_reviewer'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Reviewer',
            new_name='Review',
        ),
    ]