from django.urls import path
from . import views

urlpatterns = [
    path("", views.PolyclinicListView.as_view(), name="polyclinic-list"),
    path("create/", views.PolyclinicCreateView.as_view(), name="polyclinic-create"),
    path(
        "<int:pk>/edit/", views.PolyclinicUpdateView.as_view(), name="polyclinic-update"
    ),
    path(
        "<int:pk>/delete/",
        views.PolyclinicDeleteView.as_view(),
        name="polyclinic-delete",
    ),
]
