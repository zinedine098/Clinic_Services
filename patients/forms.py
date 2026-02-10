from django import forms
from .models import Patient


FORM_INPUT_CLASS = "w-full px-4 py-3 rounded-xl border border-slate-300 focus:ring-2 focus:ring-teal-500 focus:border-transparent transition-all duration-200"


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = [
            "medical_record_number",
            "name",
            "birth_date",
            "gender",
            "address",
            "phone",
        ]
        widgets = {
            "medical_record_number": forms.TextInput(
                attrs={
                    "class": FORM_INPUT_CLASS,
                    "placeholder": "Contoh: RM-00001",
                }
            ),
            "name": forms.TextInput(
                attrs={
                    "class": FORM_INPUT_CLASS,
                    "placeholder": "Nama lengkap pasien",
                }
            ),
            "birth_date": forms.DateInput(
                attrs={
                    "class": FORM_INPUT_CLASS,
                    "type": "date",
                }
            ),
            "gender": forms.Select(
                attrs={
                    "class": FORM_INPUT_CLASS,
                }
            ),
            "address": forms.Textarea(
                attrs={
                    "class": FORM_INPUT_CLASS,
                    "rows": 3,
                    "placeholder": "Alamat lengkap",
                }
            ),
            "phone": forms.TextInput(
                attrs={
                    "class": FORM_INPUT_CLASS,
                    "placeholder": "08xxxxxxxxxx",
                }
            ),
        }
