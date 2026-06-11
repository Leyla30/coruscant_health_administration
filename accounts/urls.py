from django.urls import path

from . import views


urlpatterns = [
    path("", views.home, name="home"),

    path(
        "register/patient/",
        views.register_patient,
        name="register_patient"
    ),

    path(
        "register/doctor/",
        views.register_doctor,
        name="register_doctor"
    ),

    path(
        "dashboard/",
        views.dashboard,
        name="dashboard"
    ),

    path(
        "profile/",
        views.profile,
        name="profile"
    ),
]