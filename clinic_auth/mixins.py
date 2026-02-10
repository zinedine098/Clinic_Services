from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect
from django.contrib import messages


class RoleRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    """Mixin to restrict access based on user role."""

    allowed_roles = []

    def test_func(self):
        if not self.request.user.is_authenticated:
            return False
        if self.request.user.role == "admin":
            return True
        return self.request.user.role in self.allowed_roles

    def handle_no_permission(self):
        messages.error(self.request, "Anda tidak memiliki akses ke halaman ini.")
        return redirect("dashboard")


class AdminRequiredMixin(RoleRequiredMixin):
    allowed_roles = ["admin"]


class LoketRequiredMixin(RoleRequiredMixin):
    allowed_roles = ["loket"]


class UGDRequiredMixin(RoleRequiredMixin):
    allowed_roles = ["ugd"]


class DokterRequiredMixin(RoleRequiredMixin):
    allowed_roles = ["dokter"]


class FarmasiRequiredMixin(RoleRequiredMixin):
    allowed_roles = ["farmasi"]
