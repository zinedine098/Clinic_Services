from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.urls import reverse_lazy
from django.shortcuts import redirect

from clinic_auth.mixins import AdminRequiredMixin
from .models import Doctor
from .forms import DoctorForm


class DoctorListView(AdminRequiredMixin, ListView):
    model = Doctor
    template_name = "doctors/list.html"
    context_object_name = "doctors"
    paginate_by = 20

    def get_queryset(self):
        return super().get_queryset().select_related("user", "polyclinic")


class DoctorCreateView(AdminRequiredMixin, CreateView):
    model = Doctor
    form_class = DoctorForm
    template_name = "doctors/form.html"
    success_url = reverse_lazy("doctor-list")

    def form_valid(self, form):
        form.save()
        messages.success(self.request, "Data dokter berhasil ditambahkan.")
        return redirect(self.success_url)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Tambah Dokter"
        context["action"] = "Simpan"
        return context


class DoctorUpdateView(AdminRequiredMixin, UpdateView):
    model = Doctor
    form_class = DoctorForm
    template_name = "doctors/form.html"
    success_url = reverse_lazy("doctor-list")

    def form_valid(self, form):
        form.save()
        messages.success(self.request, "Data dokter berhasil diperbarui.")
        return redirect(self.success_url)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Edit Dokter"
        context["action"] = "Update"
        return context


class DoctorDeleteView(AdminRequiredMixin, DeleteView):
    model = Doctor
    success_url = reverse_lazy("doctor-list")

    def post(self, request, *args, **kwargs):
        doctor = self.get_object()
        doctor.delete()
        messages.success(request, "Data dokter berhasil dihapus.")
        return redirect(self.success_url)
