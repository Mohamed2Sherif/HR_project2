# Generated by Django 4.2 on 2023-04-18 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HR', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='account',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='account',
            name='salary',
            field=models.FloatField(default=0, verbose_name='Salary'),
        ),
    ]