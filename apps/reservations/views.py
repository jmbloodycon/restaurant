from datetime import datetime

from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse_lazy
from django.utils import timezone
from django.views import View
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework import status

from .forms import ReservationForm
from .models import Reservation
from apps.tables.models import Table
from rest_framework.decorators import api_view


__all__ = (
    'ReservationCreate',
)


class ReservationCreate(View):
    model = Reservation
    success_url = reverse_lazy('dishes:dishes-list')

    def post(self, request, pk):
        user = request.user
        table = Table.objects.get(number=pk)
        table.is_booked = True
        table.save()
        self.model.objects.get_or_create(
            user=user,
            table_id=pk,
            date=datetime.now(),
            email=user.email
        )
        return HttpResponseRedirect(self.success_url)
