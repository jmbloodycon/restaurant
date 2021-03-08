from django.conf.urls import url
from django.urls import path, re_path
from django.views.generic import RedirectView

from .views import TableListView, TableDetailView

urlpatterns = [
    path('', TableListView.as_view(), name='tables-list'),
    path('<int:pk>/', TableDetailView.as_view(), name='tables-detail'),
    path('favicon\.ico$', RedirectView.as_view(url='/media/static/images/favicon.ico', permanent=True)),

]