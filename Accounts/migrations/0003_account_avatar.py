# Generated by Django 4.2.3 on 2023-07-25 13:04

import Accounts.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0002_alter_account_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to=Accounts.models.f),
        ),
    ]
