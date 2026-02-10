from django.views.generic import ListView, CreateView, DetailView
from django.contrib import messages
from django.urls import reverse_lazy
from django.shortcuts import redirect, get_object_or_404

from clinic_auth.mixins import UGDRequiredMixin
from registrations.models import Registration
from .models import Triage
from .forms import TriageForm


class TriageListView(UGDRequiredMixin, ListView):
    model = Registration
    template_name = "triage/list.html"
    context_object_name = "registrations"
    paginate_by = 20

    def get_queryset(self):
        return (
            Registration.objects.filter(status__in=["waiting_triage", "in_triage"])
            .select_related("patient")
            .order_by("created_at")
        )


class TriageCreateView(UGDRequiredMixin, CreateView):
    model = Triage
    form_class = TriageForm
    template_name = "triage/form.html"
    success_url = reverse_lazy("triage-list")

    def dispatch(self, request, *args, **kwargs):
        self.registration = get_object_or_404(
            Registration, pk=kwargs["registration_id"]
        )
        if hasattr(self.registration, "triage"):
            messages.warning(request, "Triage sudah dilakukan untuk registrasi ini.")
            return redirect("triage-list")
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        triage = form.save(commit=False)
        triage.registration = self.registration
        triage.assessed_by = self.request.user
        triage.save()
        self.registration.status = "waiting_exam"
        self.registration.save()
        messages.success(
            self.request,
            f"Triage berhasil. Pasien dirujuk ke {triage.referred_polyclinic.name}.",
        )
        return redirect(self.success_url)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["registration"] = self.registration
        context["title"] = "Triage Pasien"
        context["action"] = "Simpan Triage"
        return context


class TriageDetailView(UGDRequiredMixin, DetailView):
    model = Triage
    template_name = "triage/detail.html"
    context_object_name = "triage"
