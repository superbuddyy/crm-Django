# Generated by Django 4.1 on 2022-09-05 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("common", "0040_user_activation_key"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="key_expires",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
