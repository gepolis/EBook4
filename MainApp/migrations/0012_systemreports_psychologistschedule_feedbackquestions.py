# Generated by Django 4.2.7 on 2023-11-20 16:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('MainApp', '0011_materials_organizationscenario_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='SystemReports',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('users_count', models.IntegerField()),
                ('events_count', models.IntegerField()),
                ('classrooms_count', models.IntegerField()),
                ('teachers_count', models.IntegerField()),
                ('staffs_count', models.IntegerField()),
                ('students_count', models.IntegerField()),
                ('students_in_events_count', models.IntegerField()),
                ('accounts_have_admin_permissions', models.IntegerField()),
                ('end_events_count', models.IntegerField()),
                ('average_events_members_count', models.IntegerField()),
                ('average_members_points', models.IntegerField()),
            ],
        ),
    ]
