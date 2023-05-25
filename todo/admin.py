from django.contrib import admin
from .models import Task
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Task)
class TaskAdmin(SummernoteModelAdmin):

    summernote_field = ('description')
