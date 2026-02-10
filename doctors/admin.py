from django.contrib import admin
from .models import Doctor


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ["user", "polyclinic", "specialization", "is_active"]
    list_filter = ["polyclinic", "is_active"]
