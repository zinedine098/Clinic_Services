from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DetailView,
    DeleteView,
)
from django.contrib import messages
from django.urls import reverse_lazy
from django.db.models import Q
from django.shortcuts import redirect

from clinic_auth.mixins import RoleRequiredMixin
from .models import Patient
from .forms import PatientForm


class PatientListView(RoleRequiredMixin, ListView):
    allowed_roles = ["loket", "ugd", "dokter", "farmasi"]
    model = Patient
    template_name = "patients/list.html"
    context_object_name = "patients"
    paginate_by = 20

    def get_queryset(self):
        qs = super().get_queryset()
        search = self.request.GET.get("search", "")
        if search:
            qs = qs.filter(
                Q(medical_record_number__icontains=search)
                | Q(name__icontains=search)
                | Q(phone__icontains=search)
            )
        return qs


class PatientCreateView(RoleRequiredMixin, CreateView):
    allowed_roles = ["loket"]
    model = Patient
    form_class = PatientForm
    template_name = "patients/form.html"
    success_url = reverse_lazy("patient-list")

    def form_valid(self, form):
        form.save()
        messages.success(self.request, "Data pasien berhasil disimpan.")
        return redirect(self.success_url)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Tambah Pasien"
        context["action"] = "Simpan"
        return context


class PatientUpdateView(RoleRequiredMixin, UpdateView):
    allowed_roles = ["loket"]
    model = Patient
    form_class = PatientForm
    template_name = "patients/form.html"
    success_url = reverse_lazy("patient-list")

    def form_valid(self, form):
        form.save()
        messages.success(self.request, "Data pasien berhasil diperbarui.")
        return redirect(self.success_url)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Edit Pasien"
        context["action"] = "Update"
        return context


class PatientDetailView(RoleRequiredMixin, DetailView):
    allowed_roles = ["loket", "ugd", "dokter", "farmasi"]
    model = Patient
    template_name = "patients/detail.html"
    context_object_name = "patient"


class PatientDeleteView(RoleRequiredMixin, DeleteView):
    allowed_roles = ["loket"]
    model = Patient
    success_url = reverse_lazy("patient-list")

    def post(self, request, *args, **kwargs):
        patient = self.get_object()
        patient.delete()
        messages.success(request, "Data pasien berhasil dihapus.")
        return redirect(self.success_url)
