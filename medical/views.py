from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import (
    HealthReadingForm,
    MedicalReportForm,
    ServiceOrderForm,
    DepartmentResultForm
)


@login_required
def add_health_reading(request):
    form = HealthReadingForm(
        request.POST or None
    )

    if form.is_valid():
        reading = form.save(
            commit=False
        )

        reading.patient = request.user
        reading.save()

        return redirect("dashboard")

    return render(
        request,
        "medical/add_health_reading.html",
        {"form": form}
    )


@login_required
def create_report(request):
    form = MedicalReportForm(
        request.POST or None
    )

    if form.is_valid():
        report = form.save(
            commit=False
        )

        report.doctor = request.user
        report.patient = request.user
        report.save()

        return redirect("dashboard")

    return render(
        request,
        "medical/create_report.html",
        {"form": form}
    )


@login_required
def create_order(request):
    form = ServiceOrderForm(
        request.POST or None
    )

    if form.is_valid():
        order = form.save(
            commit=False
        )

        order.patient = request.user
        order.doctor = request.user
        order.save()

        return redirect("dashboard")

    return render(
        request,
        "medical/create_order.html",
        {"form": form}
    )


@login_required
def add_result(request):
    form = DepartmentResultForm(
        request.POST or None
    )

    if form.is_valid():
        form.save()

        return redirect("dashboard")

    return render(
        request,
        "medical/add_result.html",
        {"form": form}
    )