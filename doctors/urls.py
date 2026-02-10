from django.urls import path
from . import views

urlpatterns = [
    path("", views.DoctorListView.as_view(), name="doctor-list"),
    path("create/", views.DoctorCreateView.as_view(), name="doctor-create"),
    path("<int:pk>/edit/", views.DoctorUpdateView.as_view(), name="doctor-update"),
    path("<int:pk>/delete/", views.DoctorDeleteView.as_view(), name="doctor-delete"),
]
