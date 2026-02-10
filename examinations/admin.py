from django.contrib import admin
from .models import Examination


@admin.register(Examination)
class ExaminationAdmin(admin.ModelAdmin):
    list_display = ["id", "registration", "doctor", "created_at"]
