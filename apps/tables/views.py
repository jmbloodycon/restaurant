from django.views.generic import ListView, DetailView

from .models import Table

__all__ = (
    'TableDetailView',
    'TableListView',
)


class TableDetailView(DetailView):
    model = Table
    template_name = 'tables/detail.html'
    context_object_name = 'tables'


class TableListView(ListView):
    model = Table
    queryset = Table.objects.all()
    template_name = 'tables/list.html'
    context_object_name = 'tables'
    paginate_by = 10
