from django.contrib import admin
from .models import Medicine, Prescription


@admin.register(Medicine)
class MedicineAdmin(admin.ModelAdmin):
    list_display = ["name", "stock", "unit", "price", "is_active"]
    search_fields = ["name"]
    list_filter = ["is_active"]


@admin.register(Prescription)
class PrescriptionAdmin(admin.ModelAdmin):
    list_display = ["examination", "medicine", "dosage", "quantity", "is_dispensed"]
    list_filter = ["is_dispensed"]
