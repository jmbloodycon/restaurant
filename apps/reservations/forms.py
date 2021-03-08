from django import forms
from django.core.validators import validate_slug

from apps.reservations.models import Reservation


__all__ = (
    'ReservationForm',
)


class ReservationForm(forms.ModelForm):
    """Form for creating Reservation"""

    class Meta:
        model = Reservation
        fields = ('date',)
