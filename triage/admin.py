from django.contrib import admin
from .models import Triage


@admin.register(Triage)
class TriageAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "registration",
        "urgency_level",
        "referred_polyclinic",
        "created_at",
    ]
    list_filter = ["urgency_level"]
