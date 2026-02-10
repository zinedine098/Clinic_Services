from django.views.generic import ListView, CreateView, DetailView, DeleteView
from django.contrib import messages
from django.urls import reverse_lazy
from django.db.models import Q
from django.shortcuts import redirect

from clinic_auth.mixins import RoleRequiredMixin
from .models import Registration
from .forms import RegistrationForm


class RegistrationListView(RoleRequiredMixin, ListView):
    allowed_roles = ["loket", "ugd", "dokter", "farmasi"]
    model = Registration
    template_name = "registrations/list.html"
    context_object_name = "registrations"
    paginate_by = 20

    def get_queryset(self):
        qs = super().get_queryset().select_related("patient")
        search = self.request.GET.get("search", "")
        if search:
            qs = qs.filter(
                Q(patient__name__icontains=search)
                | Q(patient__medical_record_number__icontains=search)
            )
        status = self.request.GET.get("status", "")
        if status:
            qs = qs.filter(status=status)
        return qs


class RegistrationCreateView(RoleRequiredMixin, CreateView):
    allowed_roles = ["loket"]
    model = Registration
    form_class = RegistrationForm
    template_name = "registrations/form.html"
    success_url = reverse_lazy("registration-list")

    def form_valid(self, form):
        registration = form.save(commit=False)
        registration.queue_number = Registration.get_next_queue_number()
        registration.status = "waiting_triage"
        registration.save()
        messages.success(
            self.request,
            f"Registrasi berhasil. No. Antrian: {registration.queue_number}",
        )
        return redirect(self.success_url)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Registrasi Baru"
        context["action"] = "Daftarkan"
        return context


class RegistrationDetailView(RoleRequiredMixin, DetailView):
    allowed_roles = ["loket", "ugd", "dokter", "farmasi"]
    model = Registration
    template_name = "registrations/detail.html"
    context_object_name = "registration"

    def get_queryset(self):
        return super().get_queryset().select_related("patient")


class RegistrationCancelView(RoleRequiredMixin, DeleteView):
    allowed_roles = ["loket"]
    model = Registration
    success_url = reverse_lazy("registration-list")

    def post(self, request, *args, **kwargs):
        registration = self.get_object()
        registration.status = "cancelled"
        registration.save()
        messages.success(request, "Registrasi dibatalkan.")
        return redirect(self.success_url)
