# Generated by Django 3.1.7 on 2021-03-24 07:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("common", "0024_remove_user_company"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="apisettings",
            name="company",
        ),
        migrations.RemoveField(
            model_name="document",
            name="company",
        ),
    ]