from django.contrib import admin
from django_object_actions import DjangoObjectActions

from .models import Dish


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin, DjangoObjectActions):
    list_display = ('name', 'is_active', 'cost')
    ordering = ('cost',)
