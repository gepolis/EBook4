# Generated by Django 4.2 on 2023-06-22 14:24

import ckeditor.fields
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ClassRoom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('classroom', models.IntegerField()),
                ('parallel', models.CharField(max_length=1)),
                ('member', models.ManyToManyField(blank=True, related_name='students', to=settings.AUTH_USER_MODEL)),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teacher', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Класс',
                'verbose_name_plural': 'Классы',
            },
        ),
        migrations.CreateModel(
            name='ClassRoomsNumber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('value', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='EventCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('methodists', models.ManyToManyField(blank=True, limit_choices_to={'role': 'methodist'}, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Катигории',
            },
        ),
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(max_length=2550)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('classroom_number', models.CharField(choices=[('0', 'Детский сад'), ('1', '1 класс'), ('2', '2 класс'), ('3', '3 класс'), ('4', '4 класс'), ('5', '5 класс'), ('6', '6 класс'), ('7', '7 класс'), ('8', '8 класс'), ('9', '9 класс'), ('10', '10 класс'), ('11', '11 класс')], max_length=255, null=True)),
                ('archive', models.BooleanField(default=False)),
                ('image', models.ImageField(null=True, upload_to='images')),
                ('building', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='building', to='Accounts.building')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='category', to='MainApp.eventcategory')),
                ('organizer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='orgonizaer', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Мероприятие',
                'verbose_name_plural': 'Мероприятия',
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='Название')),
                ('content', ckeditor.fields.RichTextField(verbose_name='Содержание')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Опубликованно')),
            ],
            options={
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Новости',
            },
        ),
        migrations.CreateModel(
            name='TeacherInviteEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classroom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event_classroom', to='MainApp.classroom')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event', to='MainApp.events')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='account', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Приглашение на мероприятие',
                'verbose_name_plural': 'Приглашения на мероприятия',
            },
        ),
        migrations.CreateModel(
            name='PhotoReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='photo_reports/%Y/%m/%d/')),
                ('uploaded', models.DateTimeField(auto_now_add=True)),
                ('event', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='MainApp.events')),
            ],
        ),
        migrations.CreateModel(
            name='EventsMembers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('points', models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('is_active', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='events',
            name='volunteer',
            field=models.ManyToManyField(related_name='volunteers', to='MainApp.eventsmembers'),
        ),
    ]
