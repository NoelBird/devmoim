from django.contrib import admin
from .models import Writing

# Register your models here.
class WritingAdmin(admin.ModelAdmin):
    list_display = ["title", "content", "created_at", "updated_at"]
    filter_display = ["title", "content", "created_at", "updated_at"]

admin.site.register(Writing, WritingAdmin)