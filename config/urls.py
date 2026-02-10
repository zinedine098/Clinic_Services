from django.contrib import admin
from django.urls import path, include
from clinic_auth.views import (
    dashboard_view,
    UserListView,
    UserCreateView,
    UserUpdateView,
    UserDeleteView,
)

urlpatterns = [
    path("django-admin/", admin.site.urls),
    path("", dashboard_view, name="dashboard"),
    path("auth/", include("clinic_auth.urls")),
    path("users/", UserListView.as_view(), name="user-list"),
    path("users/create/", UserCreateView.as_view(), name="user-create"),
    path("users/<int:pk>/edit/", UserUpdateView.as_view(), name="user-update"),
    path("users/<int:pk>/delete/", UserDeleteView.as_view(), name="user-delete"),
    path("patients/", include("patients.urls")),
    path("registrations/", include("registrations.urls")),
    path("triage/", include("triage.urls")),
    path("polyclinics/", include("polyclinics.urls")),
    path("doctors/", include("doctors.urls")),
    path("examinations/", include("examinations.urls")),
    path("pharmacy/", include("pharmacy.urls")),
]
