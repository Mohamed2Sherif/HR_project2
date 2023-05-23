# Generated by Django 4.2.1 on 2023-05-21 17:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("HR", "0005_account_accid"),
    ]

    operations = [
        migrations.CreateModel(
            name="Employee",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "email",
                    models.EmailField(max_length=50, unique=True, verbose_name="email"),
                ),
                ("accId", models.IntegerField(default=0)),
                ("username", models.CharField(max_length=20, unique=True)),
                ("is_admin", models.BooleanField(default=False)),
                ("is_active", models.BooleanField(default=True)),
                ("is_staff", models.BooleanField(default=False)),
                ("is_superuser", models.BooleanField(default=False)),
                ("salary", models.FloatField(default=0, verbose_name="Salary")),
                (
                    "phone",
                    models.CharField(
                        max_length=11, null=True, verbose_name="Phone_Number"
                    ),
                ),
                ("DOB", models.DateField(null=True)),
                ("availableVac", models.IntegerField(default=0)),
                ("approvedVac", models.IntegerField(default=0)),
            ],
        ),
    ]