# Generated by Django 4.0 on 2023-07-27 17:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0005_photoreport_author_photoreport_deleted_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacherinviteevent',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event_teacher', to='MainApp.events'),
        ),
    ]
