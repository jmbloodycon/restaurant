from django.views.generic import ListView, DetailView

from .models import Dish

__all__ = (
    'DishDetailView',
    'DishListView',
)


class DishDetailView(DetailView):
    model = Dish
    template_name = 'dishes/detail.html'
    context_object_name = 'dishes'
    paginate_by = 2


class DishListView(ListView):
    model = Dish
    queryset = Dish.objects.all()
    template_name = 'dishes/list.html'
    context_object_name = 'dishes'
    paginate_by = 10
