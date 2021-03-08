from django.urls import path, re_path
from .views import ReservationCreate

urlpatterns = [
    path('<int:pk>', ReservationCreate.as_view(), name='reservation'),
]
