from django import forms
from .models import Medicine, Prescription


FORM_INPUT_CLASS = "w-full px-4 py-3 rounded-xl border border-slate-300 focus:ring-2 focus:ring-teal-500 focus:border-transparent transition-all duration-200"


class MedicineForm(forms.ModelForm):
    class Meta:
        model = Medicine
        fields = ["name", "description", "stock", "unit", "price", "is_active"]
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": FORM_INPUT_CLASS,
                    "placeholder": "Nama obat",
                }
            ),
            "description": forms.Textarea(
                attrs={
                    "class": FORM_INPUT_CLASS,
                    "rows": 3,
                    "placeholder": "Deskripsi obat",
                }
            ),
            "stock": forms.NumberInput(
                attrs={
                    "class": FORM_INPUT_CLASS,
                    "placeholder": "0",
                }
            ),
            "unit": forms.TextInput(
                attrs={
                    "class": FORM_INPUT_CLASS,
                    "placeholder": "tablet / kapsul / botol",
                }
            ),
            "price": forms.NumberInput(
                attrs={
                    "class": FORM_INPUT_CLASS,
                    "placeholder": "0",
                    "step": "100",
                }
            ),
            "is_active": forms.CheckboxInput(
                attrs={
                    "class": "rounded border-slate-300 text-teal-600 focus:ring-teal-500 h-5 w-5",
                }
            ),
        }


class PrescriptionForm(forms.ModelForm):
    class Meta:
        model = Prescription
        fields = ["medicine", "dosage", "quantity", "instructions"]
        widgets = {
            "medicine": forms.Select(
                attrs={
                    "class": FORM_INPUT_CLASS,
                }
            ),
            "dosage": forms.TextInput(
                attrs={
                    "class": FORM_INPUT_CLASS,
                    "placeholder": "Contoh: 3x1 sehari",
                }
            ),
            "quantity": forms.NumberInput(
                attrs={
                    "class": FORM_INPUT_CLASS,
                    "placeholder": "10",
                }
            ),
            "instructions": forms.Textarea(
                attrs={
                    "class": FORM_INPUT_CLASS,
                    "rows": 2,
                    "placeholder": "Aturan pakai obat",
                }
            ),
        }
