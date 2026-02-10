from django.contrib import admin
from .models import Patient


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ["medical_record_number", "name", "gender", "phone", "created_at"]
    search_fields = ["medical_record_number", "name", "phone"]
    list_filter = ["gender"]
