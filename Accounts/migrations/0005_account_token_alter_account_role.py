# Generated by Django 4.0 on 2023-08-02 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0004_alter_account_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='token',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='role',
            field=models.TextField(choices=[('admin', 'Администратор'), ('teacher', 'Учитель'), ('parent', 'Родитель'), ('student', 'Ученик'), ('methodist', 'Методист'), ('director', 'Директор'), ('head_teacher', 'Завуч'), ('psychologist', 'Психолог')], max_length=20, null=True),
        ),
    ]
