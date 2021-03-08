from django.urls import path
from apps.users.views import UserProfileView, UserProfileUpdateView
urlpatterns = [
    path('edit/<int:pk>/', UserProfileUpdateView.as_view(), name='edit'),
    path('profile/<int:pk>/', UserProfileView.as_view(), name='profile'),

]
