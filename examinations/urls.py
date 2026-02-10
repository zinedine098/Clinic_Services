from django.urls import path
from . import views

urlpatterns = [
    path("", views.ExaminationListView.as_view(), name="examination-list"),
    path(
        "<int:registration_id>/create/",
        views.ExaminationCreateView.as_view(),
        name="examination-create",
    ),
    path(
        "<int:pk>/detail/",
        views.ExaminationDetailView.as_view(),
        name="examination-detail",
    ),
]
