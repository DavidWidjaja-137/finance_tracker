# Generated by Django 5.0.6 on 2024-05-21 00:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("finance", "0002_auto_20240518_2235"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="transactionmap",
            unique_together={("name", "type")},
        ),
    ]
