# Generated by Django 4.2.1 on 2023-05-22 11:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HR', '0011_remove_account_salary'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='Birth_date',
            new_name='DOB',
        ),
    ]
