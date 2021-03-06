# Generated by Django 4.0.4 on 2022-05-11 09:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import taskapp.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Sprint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(blank=True, default=0, max_length=150, null=True)),
                ('status', models.CharField(choices=[('active', 'active'), ('inactive', 'inactive')], max_length=120)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_number', models.IntegerField()),
                ('description', models.CharField(blank=True, max_length=150, null=True)),
                ('status', models.CharField(choices=[('STATUS_TODO', 'Not Started'), ('STATUS_IN_PROGRESS', 'In Progress'), ('STATUS_COMPLETED', 'Completed'), ('STATUS_DONE', 'Done')], default='STATUS_TODO', max_length=120)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to=taskapp.models.Task.nameFile)),
                ('backlog', models.BooleanField()),
                ('sprint', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='taskapp.sprint')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
