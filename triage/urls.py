from django.urls import path
from . import views

urlpatterns = [
    path("", views.TriageListView.as_view(), name="triage-list"),
    path(
        "<int:registration_id>/create/",
        views.TriageCreateView.as_view(),
        name="triage-create",
    ),
    path("<int:pk>/detail/", views.TriageDetailView.as_view(), name="triage-detail"),
]
