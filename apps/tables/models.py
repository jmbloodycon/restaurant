from django.core.validators import validate_slug
from django.db import models
from django.utils.translation import ugettext_lazy as _


__all__ = (
    'Table',
)


class Table(models.Model):
    number = models.IntegerField(
        verbose_name=_('Номер столика')
    )
    capacity = models.IntegerField(
        verbose_name=_('Вместимость столика')
    )
    is_booked = models.BooleanField(
        verbose_name=_('Забронирован'),
        default=False
    )

    class Meta:
        verbose_name = _('Table')
        verbose_name_plural = _('Tables')
        ordering = ['number']

    def __str__(self):
        return f'Table {self.number}'
