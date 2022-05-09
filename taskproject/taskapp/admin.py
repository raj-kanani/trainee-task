from django.contrib import admin
from .models import *


@admin.register(Sprint)
class SprintAdmin(admin.ModelAdmin):
    list_display = ['id', 'number', 'status', 'start_date', 'end_date']


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'task_number', 'description', 'sprint', 'user', 'status', 'start_date', 'image']
