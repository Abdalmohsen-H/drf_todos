from django.contrib import admin

# Register your models here to be able to manage it from django admin dashboard.
from .models import Task

admin.site.register(Task)
