from django.urls import path
from . import views

urlpatterns = [
    path("queue/", views.PharmacyQueueView.as_view(), name="pharmacy-queue"),
    path(
        "<int:pk>/dispense/",
        views.PharmacyDispenseView.as_view(),
        name="pharmacy-dispense",
    ),
    path("medicines/", views.MedicineListView.as_view(), name="medicine-list"),
    path(
        "medicines/create/", views.MedicineCreateView.as_view(), name="medicine-create"
    ),
    path(
        "medicines/<int:pk>/edit/",
        views.MedicineUpdateView.as_view(),
        name="medicine-update",
    ),
    path(
        "medicines/<int:pk>/delete/",
        views.MedicineDeleteView.as_view(),
        name="medicine-delete",
    ),
]
