# Generated by Django 4.2 on 2023-05-22 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0035_permissions_alter_otps_code_roles_account_roles'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='role',
        ),
        migrations.AlterField(
            model_name='otps',
            name='code',
            field=models.IntegerField(default=673637),
        ),
    ]
