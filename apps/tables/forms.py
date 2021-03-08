from django import forms

from apps.tables.models import Table


__all__ = (
    'TableForm',
)


class TableForm(forms.ModelForm):
    class Meta:
        model = Table
        fields = ('number', )
