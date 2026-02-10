from django.contrib import admin
from .models import Registration


@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    list_display = ["id", "patient", "queue_number", "status", "created_at"]
    list_filter = ["status"]
    search_fields = ["patient__name", "patient__medical_record_number"]
