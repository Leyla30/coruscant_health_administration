from django import forms

from .models import (
    HealthReading,
    MedicalReport,
    ServiceOrder,
    DepartmentResult
)


class HealthReadingForm(forms.ModelForm):
    class Meta:
        model = HealthReading
        fields = [
            "temperature",
            "heart_rate",
            "oxygen_level",
            "blood_pressure"
        ]


class MedicalReportForm(forms.ModelForm):
    class Meta:
        model = MedicalReport
        fields = [
            "diagnosis",
            "recommendations"
        ]


class ServiceOrderForm(forms.ModelForm):
    class Meta:
        model = ServiceOrder
        fields = [
            "order_type"
        ]


class DepartmentResultForm(forms.ModelForm):
    class Meta:
        model = DepartmentResult
        fields = [
            "result_text"
        ]