# Generated by Django 4.2 on 2023-04-18 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HR', '0002_account_is_active_account_is_superuser_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='email',
            field=models.EmailField(max_length=50, unique=True, verbose_name='email'),
        ),
    ]
