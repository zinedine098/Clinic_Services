from django.views.generic import ListView, CreateView, DetailView
from django.contrib import messages
from django.urls import reverse_lazy
from django.shortcuts import redirect, get_object_or_404

from clinic_auth.mixins import DokterRequiredMixin
from registrations.models import Registration
from doctors.models import Doctor
from pharmacy.models import Prescription
from pharmacy.forms import PrescriptionForm
from .models import Examination
from .forms import ExaminationForm


class ExaminationListView(DokterRequiredMixin, ListView):
    model = Registration
    template_name = "examinations/list.html"
    context_object_name = "registrations"
    paginate_by = 20

    def get_queryset(self):
        return (
            Registration.objects.filter(status__in=["waiting_exam", "in_exam"])
            .select_related("patient")
            .order_by("created_at")
        )


class ExaminationCreateView(DokterRequiredMixin, CreateView):
    model = Examination
    form_class = ExaminationForm
    template_name = "examinations/form.html"
    success_url = reverse_lazy("examination-list")

    def dispatch(self, request, *args, **kwargs):
        self.registration = get_object_or_404(
            Registration, pk=kwargs["registration_id"]
        )
        if hasattr(self.registration, "examination"):
            messages.warning(
                request, "Pemeriksaan sudah dilakukan untuk registrasi ini."
            )
            return redirect("examination-list")
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["registration"] = self.registration
        context["title"] = "Pemeriksaan Pasien"
        context["action"] = "Simpan Pemeriksaan"
        context["prescription_form"] = PrescriptionForm()
        return context

    def form_valid(self, form):
        try:
            doctor = self.request.user.doctor_profile
        except Doctor.DoesNotExist:
            messages.error(self.request, "Profil dokter belum terdaftar.")
            return redirect("examination-list")

        examination = form.save(commit=False)
        examination.registration = self.registration
        examination.doctor = doctor
        examination.save()

        # Process prescriptions
        medicine_ids = self.request.POST.getlist("prescription_medicine")
        dosages = self.request.POST.getlist("prescription_dosage")
        quantities = self.request.POST.getlist("prescription_quantity")
        instructions_list = self.request.POST.getlist("prescription_instructions")

        for i in range(len(medicine_ids)):
            if medicine_ids[i]:
                Prescription.objects.create(
                    examination=examination,
                    medicine_id=int(medicine_ids[i]),
                    dosage=dosages[i] if i < len(dosages) else "",
                    quantity=(
                        int(quantities[i])
                        if i < len(quantities) and quantities[i]
                        else 1
                    ),
                    instructions=(
                        instructions_list[i] if i < len(instructions_list) else ""
                    ),
                )

        self.registration.status = "waiting_pharmacy"
        self.registration.save()
        messages.success(self.request, "Pemeriksaan berhasil disimpan.")
        return redirect(self.success_url)


class ExaminationDetailView(DokterRequiredMixin, DetailView):
    model = Examination
    template_name = "examinations/detail.html"
    context_object_name = "examination"

    def get_queryset(self):
        return (
            super()
            .get_queryset()
            .select_related("registration__patient", "doctor__user")
        )
