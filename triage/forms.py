from django import forms
from .models import Triage
from polyclinics.models import Polyclinic


FORM_INPUT_CLASS = "w-full px-4 py-3 rounded-xl border border-slate-300 focus:ring-2 focus:ring-teal-500 focus:border-transparent transition-all duration-200"


class TriageForm(forms.ModelForm):
    class Meta:
        model = Triage
        fields = [
            "complaint",
            "blood_pressure",
            "temperature",
            "heart_rate",
            "weight",
            "height",
            "urgency_level",
            "referred_polyclinic",
        ]
        widgets = {
            "complaint": forms.Textarea(
                attrs={
                    "class": FORM_INPUT_CLASS,
                    "rows": 3,
                    "placeholder": "Keluhan pasien",
                }
            ),
            "blood_pressure": forms.TextInput(
                attrs={
                    "class": FORM_INPUT_CLASS,
                    "placeholder": "Contoh: 120/80",
                }
            ),
            "temperature": forms.NumberInput(
                attrs={
                    "class": FORM_INPUT_CLASS,
                    "placeholder": "36.5",
                    "step": "0.1",
                }
            ),
            "heart_rate": forms.NumberInput(
                attrs={
                    "class": FORM_INPUT_CLASS,
                    "placeholder": "80",
                }
            ),
            "weight": forms.NumberInput(
                attrs={
                    "class": FORM_INPUT_CLASS,
                    "placeholder": "65.0",
                    "step": "0.1",
                }
            ),
            "height": forms.NumberInput(
                attrs={
                    "class": FORM_INPUT_CLASS,
                    "placeholder": "170.0",
                    "step": "0.1",
                }
            ),
            "urgency_level": forms.Select(
                attrs={
                    "class": FORM_INPUT_CLASS,
                }
            ),
            "referred_polyclinic": forms.Select(
                attrs={
                    "class": FORM_INPUT_CLASS,
                }
            ),
        }
