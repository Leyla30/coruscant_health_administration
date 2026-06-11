from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import User, PatientProfile, DoctorProfile


class PatientRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    birth_date = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={"type": "date"})
    )

    emergency_contact = forms.CharField(
        required=False,
        max_length=120
    )

    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "password1",
            "password2"
        )

    def save(self, commit=True):
        user = super().save(commit=False)

        user.email = self.cleaned_data["email"]
        user.role = "patient"

        # Lala:
        # accounts are reviewed by admin before activation
        user.approved = False

        if commit:
            user.save()

            PatientProfile.objects.create(
                user=user,
                birth_date=self.cleaned_data.get("birth_date"),
                emergency_contact=self.cleaned_data.get(
                    "emergency_contact"
                )
            )

        return user


class DoctorRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    specialty = forms.CharField(
        max_length=120
    )

    license_number = forms.CharField(
        max_length=60
    )

    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "password1",
            "password2"
        )

    def save(self, commit=True):
        user = super().save(commit=False)

        user.email = self.cleaned_data["email"]
        user.role = "doctor"

        # Lala:
        # doctor accounts should be approved manually
        user.approved = False

        if commit:
            user.save()

            DoctorProfile.objects.create(
                user=user,
                specialty=self.cleaned_data["specialty"],
                license_number=self.cleaned_data["license_number"]
            )

        return user