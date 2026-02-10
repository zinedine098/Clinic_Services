from django import forms
from .models import Doctor
from polyclinics.models import Polyclinic
from clinic_auth.models import User


FORM_INPUT_CLASS = "w-full px-4 py-3 rounded-xl border border-slate-300 focus:ring-2 focus:ring-teal-500 focus:border-transparent transition-all duration-200"


class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ["user", "polyclinic", "specialization", "license_number", "is_active"]
        widgets = {
            "user": forms.Select(
                attrs={
                    "class": FORM_INPUT_CLASS,
                }
            ),
            "polyclinic": forms.Select(
                attrs={
                    "class": FORM_INPUT_CLASS,
                }
            ),
            "specialization": forms.TextInput(
                attrs={
                    "class": FORM_INPUT_CLASS,
                    "placeholder": "Spesialisasi dokter",
                }
            ),
            "license_number": forms.TextInput(
                attrs={
                    "class": FORM_INPUT_CLASS,
                    "placeholder": "Nomor SIP",
                }
            ),
            "is_active": forms.CheckboxInput(
                attrs={
                    "class": "rounded border-slate-300 text-teal-600 focus:ring-teal-500 h-5 w-5",
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["user"].queryset = User.objects.filter(role="dokter")
