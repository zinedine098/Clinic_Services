from django.urls import path
from . import views

urlpatterns = [
    path("", views.RegistrationListView.as_view(), name="registration-list"),
    path("create/", views.RegistrationCreateView.as_view(), name="registration-create"),
    path(
        "<int:pk>/", views.RegistrationDetailView.as_view(), name="registration-detail"
    ),
    path(
        "<int:pk>/cancel/",
        views.RegistrationCancelView.as_view(),
        name="registration-cancel",
    ),
]
