from django import forms
from .models import Polyclinic


FORM_INPUT_CLASS = "w-full px-4 py-3 rounded-xl border border-slate-300 focus:ring-2 focus:ring-teal-500 focus:border-transparent transition-all duration-200"


class PolyclinicForm(forms.ModelForm):
    class Meta:
        model = Polyclinic
        fields = ["name", "description", "is_active"]
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": FORM_INPUT_CLASS,
                    "placeholder": "Nama poliklinik",
                }
            ),
            "description": forms.Textarea(
                attrs={
                    "class": FORM_INPUT_CLASS,
                    "rows": 3,
                    "placeholder": "Deskripsi (opsional)",
                }
            ),
            "is_active": forms.CheckboxInput(
                attrs={
                    "class": "rounded border-slate-300 text-teal-600 focus:ring-teal-500 h-5 w-5",
                }
            ),
        }
