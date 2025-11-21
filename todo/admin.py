from django.contrib import admin
from .models import Todo


@admin.register(Todo)

class TodoAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'created_at']
    search_fields = ['title', 'desc']
    list_filter = ['created_at', 'status']
    
