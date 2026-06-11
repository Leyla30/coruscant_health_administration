from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import (
    PatientRegistrationForm,
    DoctorRegistrationForm
)


def home(request):
    return render(request, "accounts/home.html")


def register_patient(request):
    if request.method == "POST":
        form = PatientRegistrationForm(request.POST)

        if form.is_valid():
            form.save()

            messages.success(
                request,
                "Account created. Please wait for administrator approval."
            )

            return redirect("login")
    else:
        form = PatientRegistrationForm()

    return render(
        request,
        "accounts/register_patient.html",
        {"form": form}
    )


def register_doctor(request):
    if request.method == "POST":
        form = DoctorRegistrationForm(request.POST)

        if form.is_valid():
            form.save()

            messages.success(
                request,
                "Doctor account created successfully."
            )

            return redirect("login")
    else:
        form = DoctorRegistrationForm()

    return render(
        request,
        "accounts/register_doctor.html",
        {"form": form}
    )


@login_required
def dashboard(request):
    current_user = request.user

    # Lala:
    # simple dashboard depending on user role

    context = {
        "current_user": current_user
    }

    return render(
        request,
        "accounts/dashboard.html",
        context
    )


@login_required
def profile(request):
    return render(
        request,
        "accounts/profile.html",
        {
            "user_data": request.user
        }
    )