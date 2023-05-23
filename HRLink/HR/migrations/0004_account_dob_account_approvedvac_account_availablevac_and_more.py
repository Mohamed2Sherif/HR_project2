# Generated by Django 4.2 on 2023-04-19 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HR', '0003_alter_account_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='DOB',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='account',
            name='approvedVac',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='account',
            name='availableVac',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='account',
            name='phone',
            field=models.CharField(max_length=11, null=True, verbose_name='Phone_Number'),
        ),
    ]