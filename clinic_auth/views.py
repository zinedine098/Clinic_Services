from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.urls import reverse_lazy
from django.db.models import Count, Q
from django.utils import timezone

from .forms import LoginForm, UserForm
from .models import User
from .mixins import AdminRequiredMixin
from registrations.models import Registration
from patients.models import Patient
from pharmacy.models import Medicine, Prescription


def login_view(request):
    if request.user.is_authenticated:
        return redirect("dashboard")
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(
                request, f"Selamat datang, {user.get_full_name() or user.username}!"
            )
            return redirect("dashboard")
        else:
            messages.error(request, "Username atau password salah.")
    else:
        form = LoginForm()
    return render(request, "auth/login.html", {"form": form})


@login_required
def logout_view(request):
    logout(request)
    messages.info(request, "Anda telah berhasil keluar.")
    return redirect("login")


@login_required
def dashboard_view(request):
    today = timezone.now().date()
    context = {
        "total_patients": Patient.objects.count(),
        "today_registrations": Registration.objects.filter(
            created_at__date=today
        ).count(),
        "waiting_triage": Registration.objects.filter(status="waiting_triage").count(),
        "waiting_exam": Registration.objects.filter(status="waiting_exam").count(),
        "waiting_pharmacy": Registration.objects.filter(
            status="waiting_pharmacy"
        ).count(),
        "completed_today": Registration.objects.filter(
            status="completed", created_at__date=today
        ).count(),
        "total_medicines": Medicine.objects.count(),
        "low_stock_medicines": Medicine.objects.filter(stock__lte=10).count(),
        "recent_registrations": Registration.objects.select_related("patient").order_by(
            "-created_at"
        )[:10],
    }
    return render(request, "dashboard/index.html", context)


class UserListView(AdminRequiredMixin, ListView):
    model = User
    template_name = "users/list.html"
    context_object_name = "users"
    paginate_by = 20

    def get_queryset(self):
        qs = super().get_queryset()
        search = self.request.GET.get("search", "")
        if search:
            qs = qs.filter(
                Q(username__icontains=search)
                | Q(first_name__icontains=search)
                | Q(last_name__icontains=search)
                | Q(email__icontains=search)
            )
        role = self.request.GET.get("role", "")
        if role:
            qs = qs.filter(role=role)
        return qs


class UserCreateView(AdminRequiredMixin, CreateView):
    model = User
    form_class = UserForm
    template_name = "users/form.html"
    success_url = reverse_lazy("user-list")

    def form_valid(self, form):
        user = form.save(commit=False)
        password = form.cleaned_data.get("password")
        if password:
            user.set_password(password)
        else:
            user.set_password("password123")
        user.save()
        messages.success(self.request, f"User {user.username} berhasil dibuat.")
        return redirect(self.success_url)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Tambah User"
        context["action"] = "Simpan"
        return context


class UserUpdateView(AdminRequiredMixin, UpdateView):
    model = User
    form_class = UserForm
    template_name = "users/form.html"
    success_url = reverse_lazy("user-list")

    def form_valid(self, form):
        user = form.save()
        messages.success(self.request, f"User {user.username} berhasil diperbarui.")
        return redirect(self.success_url)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Edit User"
        context["action"] = "Update"
        return context


class UserDeleteView(AdminRequiredMixin, DeleteView):
    model = User
    success_url = reverse_lazy("user-list")

    def post(self, request, *args, **kwargs):
        user = self.get_object()
        username = user.username
        user.delete()
        messages.success(request, f"User {username} berhasil dihapus.")
        return redirect(self.success_url)
