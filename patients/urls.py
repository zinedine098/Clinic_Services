from django.urls import path
from . import views

urlpatterns = [
    path("", views.PatientListView.as_view(), name="patient-list"),
    path("create/", views.PatientCreateView.as_view(), name="patient-create"),
    path("<int:pk>/", views.PatientDetailView.as_view(), name="patient-detail"),
    path("<int:pk>/edit/", views.PatientUpdateView.as_view(), name="patient-update"),
    path("<int:pk>/delete/", views.PatientDeleteView.as_view(), name="patient-delete"),
]
