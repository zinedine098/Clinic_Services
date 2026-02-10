from django.contrib import admin
from .models import Polyclinic


@admin.register(Polyclinic)
class PolyclinicAdmin(admin.ModelAdmin):
    list_display = ["name", "is_active", "created_at"]
