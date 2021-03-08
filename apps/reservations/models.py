from django.core.validators import validate_slug
from django.db import models
from django.utils.translation import ugettext_lazy as _


__all__ = (
    'Reservation',
)


class Reservation(models.Model):
    user = models.ForeignKey(
        'users.User',
        related_name='reservations',
        on_delete=models.CASCADE
    )
    table = models.ForeignKey(
        'tables.Table',
        related_name='reservations',
        on_delete=models.CASCADE
    )
    date = models.DateTimeField(
        verbose_name=_("Reservation's description")
    )
    email = models.EmailField(
        verbose_name=_("User Email")

    )

    class Meta:
        verbose_name = _("Reservation")
        verbose_name_plural = _("Reservations")

    def __str__(self):
        return f'{self.user} {self.date}'
