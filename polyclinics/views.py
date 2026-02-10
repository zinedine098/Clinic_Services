from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.urls import reverse_lazy
from django.shortcuts import redirect

from clinic_auth.mixins import AdminRequiredMixin
from .models import Polyclinic
from .forms import PolyclinicForm


class PolyclinicListView(AdminRequiredMixin, ListView):
    model = Polyclinic
    template_name = "polyclinics/list.html"
    context_object_name = "polyclinics"
    paginate_by = 20


class PolyclinicCreateView(AdminRequiredMixin, CreateView):
    model = Polyclinic
    form_class = PolyclinicForm
    template_name = "polyclinics/form.html"
    success_url = reverse_lazy("polyclinic-list")

    def form_valid(self, form):
        form.save()
        messages.success(self.request, "Poliklinik berhasil ditambahkan.")
        return redirect(self.success_url)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Tambah Poliklinik"
        context["action"] = "Simpan"
        return context


class PolyclinicUpdateView(AdminRequiredMixin, UpdateView):
    model = Polyclinic
    form_class = PolyclinicForm
    template_name = "polyclinics/form.html"
    success_url = reverse_lazy("polyclinic-list")

    def form_valid(self, form):
        form.save()
        messages.success(self.request, "Poliklinik berhasil diperbarui.")
        return redirect(self.success_url)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Edit Poliklinik"
        context["action"] = "Update"
        return context


class PolyclinicDeleteView(AdminRequiredMixin, DeleteView):
    model = Polyclinic
    success_url = reverse_lazy("polyclinic-list")

    def post(self, request, *args, **kwargs):
        polyclinic = self.get_object()
        polyclinic.delete()
        messages.success(request, "Poliklinik berhasil dihapus.")
        return redirect(self.success_url)
