# Generated by Django 5.0.6 on 2024-05-21 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("finance", "0003_alter_transactionmap_unique_together"),
    ]

    operations = [
        migrations.AlterField(
            model_name="transactionmap",
            name="name",
            field=models.CharField(max_length=200),
        ),
    ]
