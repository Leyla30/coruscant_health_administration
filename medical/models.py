from django.db import models
from accounts.models import User


class HealthReading(models.Model):
    patient = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="health_readings"
    )

    temperature = models.DecimalField(
        max_digits=4,
        decimal_places=1
    )

    heart_rate = models.IntegerField()

    oxygen_level = models.IntegerField()

    blood_pressure = models.CharField(
        max_length=20
    )

    recorded_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.patient.username} reading"


class MedicalReport(models.Model):
    patient = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="medical_reports"
    )

    doctor = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="doctor_reports"
    )

    diagnosis = models.TextField()

    recommendations = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    # Leyla:
    # doctors leave notes after reviewing patient data

    def __str__(self):
        return f"Report for {self.patient.username}"


class ServiceOrder(models.Model):
    ORDER_TYPES = (
        ("ct", "CT Scan"),
        ("pet", "PET Scan"),
        ("mri", "MRI"),
        ("blood", "Blood Test"),
    )

    patient = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    doctor = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="service_orders"
    )

    order_type = models.CharField(
        max_length=20,
        choices=ORDER_TYPES
    )

    completed = models.BooleanField(
        default=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.order_type


class DepartmentResult(models.Model):
    order = models.OneToOneField(
        ServiceOrder,
        on_delete=models.CASCADE
    )

    result_text = models.TextField()

    uploaded_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"Result #{self.order.id}"


class EncryptedDocument(models.Model):
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    document = models.FileField(
        upload_to="medical_documents/"
    )

    encrypted = models.BooleanField(
        default=True
    )

    uploaded_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.document.name