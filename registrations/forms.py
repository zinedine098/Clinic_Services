from django import forms
from .models import Registration
from patients.models import Patient


FORM_INPUT_CLASS = "w-full px-4 py-3 rounded-xl border border-slate-300 focus:ring-2 focus:ring-teal-500 focus:border-transparent transition-all duration-200"


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ["patient", "notes"]
        widgets = {
            "patient": forms.Select(
                attrs={
                    "class": FORM_INPUT_CLASS,
                }
            ),
            "notes": forms.Textarea(
                attrs={
                    "class": FORM_INPUT_CLASS,
                    "rows": 3,
                    "placeholder": "Catatan tambahan (opsional)",
                }
            ),
        }
