from django.db import models
from django.utils.translation import ugettext_lazy as _

__all__ = (
    'Dish',
)


class Dish(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name=_("Name"),
    )
    description = models.TextField(
        max_length=255,
        verbose_name=_("Description"),
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name=_("Is active"),
    )
    cost = models.FloatField(
        default=10,
        verbose_name=_('Стоимость')
    )
    photo = models.ImageField(
        upload_to='static/imagination',
        verbose_name='Photo',
        help_text=_("Dish's photo.")
    )

    class Meta:
        ordering = ('name',)
        verbose_name = _("Dish")
        verbose_name_plural = _("Dishes")

    def __str__(self):
        return self.name
