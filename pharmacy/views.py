from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DetailView,
    DeleteView,
)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.urls import reverse_lazy
from django.shortcuts import redirect, get_object_or_404
from django.utils import timezone
from django.db.models import Q

from clinic_auth.mixins import FarmasiRequiredMixin, AdminRequiredMixin
from registrations.models import Registration
from .models import Medicine, Prescription
from .forms import MedicineForm


class PharmacyQueueView(FarmasiRequiredMixin, ListView):
    model = Registration
    template_name = "pharmacy/queue.html"
    context_object_name = "registrations"
    paginate_by = 20

    def get_queryset(self):
        return (
            Registration.objects.filter(status="waiting_pharmacy")
            .select_related("patient")
            .order_by("created_at")
        )


class PharmacyDispenseView(FarmasiRequiredMixin, DetailView):
    model = Registration
    template_name = "pharmacy/dispense.html"
    context_object_name = "registration"

    def get_queryset(self):
        return Registration.objects.select_related(
            "patient", "examination__doctor__user"
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        registration = self.get_object()
        if hasattr(registration, "examination"):
            context["prescriptions"] = (
                registration.examination.prescriptions.select_related("medicine").all()
            )
        return context

    def post(self, request, *args, **kwargs):
        registration = self.get_object()
        if hasattr(registration, "examination"):
            prescriptions = registration.examination.prescriptions.select_related(
                "medicine"
            ).all()
            for prescription in prescriptions:
                if not prescription.is_dispensed:
                    if prescription.medicine.stock >= prescription.quantity:
                        prescription.medicine.stock -= prescription.quantity
                        prescription.medicine.save()
                        prescription.is_dispensed = True
                        prescription.dispensed_by = request.user
                        prescription.dispensed_at = timezone.now()
                        prescription.save()
                    else:
                        messages.error(
                            request,
                            f"Stok {prescription.medicine.name} tidak mencukupi.",
                        )
                        return redirect("pharmacy-dispense", pk=registration.pk)

        registration.status = "completed"
        registration.save()
        messages.success(request, "Obat berhasil diserahkan. Registrasi selesai.")
        return redirect("pharmacy-queue")


# Medicine CRUD (Admin / Farmasi)
class MedicineListView(LoginRequiredMixin, ListView):
    model = Medicine
    template_name = "pharmacy/medicine_list.html"
    context_object_name = "medicines"
    paginate_by = 20

    def get_queryset(self):
        qs = super().get_queryset()
        search = self.request.GET.get("search", "")
        if search:
            qs = qs.filter(Q(name__icontains=search))
        return qs


class MedicineCreateView(AdminRequiredMixin, CreateView):
    model = Medicine
    form_class = MedicineForm
    template_name = "pharmacy/medicine_form.html"
    success_url = reverse_lazy("medicine-list")

    def form_valid(self, form):
        form.save()
        messages.success(self.request, "Obat berhasil ditambahkan.")
        return redirect(self.success_url)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Tambah Obat"
        context["action"] = "Simpan"
        return context


class MedicineUpdateView(AdminRequiredMixin, UpdateView):
    model = Medicine
    form_class = MedicineForm
    template_name = "pharmacy/medicine_form.html"
    success_url = reverse_lazy("medicine-list")

    def form_valid(self, form):
        form.save()
        messages.success(self.request, "Data obat berhasil diperbarui.")
        return redirect(self.success_url)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Edit Obat"
        context["action"] = "Update"
        return context


class MedicineDeleteView(AdminRequiredMixin, DeleteView):
    model = Medicine
    success_url = reverse_lazy("medicine-list")

    def post(self, request, *args, **kwargs):
        medicine = self.get_object()
        medicine.delete()
        messages.success(request, "Data obat berhasil dihapus.")
        return redirect(self.success_url)
