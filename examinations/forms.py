from django import forms
from .models import Examination


FORM_INPUT_CLASS = "w-full px-4 py-3 rounded-xl border border-slate-300 focus:ring-2 focus:ring-teal-500 focus:border-transparent transition-all duration-200"


class ExaminationForm(forms.ModelForm):
    class Meta:
        model = Examination
        fields = ["diagnosis", "notes", "treatment"]
        widgets = {
            "diagnosis": forms.Textarea(
                attrs={
                    "class": FORM_INPUT_CLASS,
                    "rows": 3,
                    "placeholder": "Diagnosis pasien",
                }
            ),
            "notes": forms.Textarea(
                attrs={
                    "class": FORM_INPUT_CLASS,
                    "rows": 3,
                    "placeholder": "Catatan pemeriksaan",
                }
            ),
            "treatment": forms.Textarea(
                attrs={
                    "class": FORM_INPUT_CLASS,
                    "rows": 3,
                    "placeholder": "Tindakan yang dilakukan",
                }
            ),
        }
