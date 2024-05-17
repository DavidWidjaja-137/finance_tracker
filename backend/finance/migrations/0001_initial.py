# Generated by Django 5.0.6 on 2024-05-17 01:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='TransactionCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='TransactionMap',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('description', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('amount', models.FloatField()),
                ('flow', models.CharField(choices=[('INFLOW', 'Inflow'), ('OUTFLOW', 'Outflow')], max_length=10)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='finance.account')),
                ('mapping', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='finance.transactionmap')),
            ],
        ),
        migrations.CreateModel(
            name='TransactionType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.CharField(max_length=200)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='finance.transactioncategory')),
            ],
        ),
        migrations.AddField(
            model_name='transactionmap',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='finance.transactiontype'),
        ),
    ]
