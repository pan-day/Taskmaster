from django.contrib import admin
from .models import Task  # импортируем нашу модель под название Task


admin.site.register(Task)  # регестрируем модель Task
