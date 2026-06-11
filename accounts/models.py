from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    ROLE_CHOICES = (
        ("patient", "Patient"),
        ("doctor", "Doctor"),
        ("department", "Department"),
        ("admin", "Admin"),
        ("emergency", "Emergency"),
    )

    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.username


class PatientProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    birth_date = models.DateField(
        null=True,
        blank=True
    )

    emergency_contact = models.CharField(
        max_length=120,
        blank=True
    )

    # Lala:
    # patients often provide emergency numbers later
    notes = models.TextField(
        blank=True
    )

    def __str__(self):
        return self.user.username


class DoctorProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    specialty = models.CharField(
        max_length=120
    )

    license_number = models.CharField(
        max_length=60
    )

    def __str__(self):
        return f"Dr. {self.user.username}"