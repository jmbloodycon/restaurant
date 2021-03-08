from django.urls import reverse_lazy
from django.views.generic import DetailView, UpdateView

from .models import User
from .forms import CustomUserChangeForm

__all__ = (
    'UserProfileUpdateView',
    'UserProfileView'
)


class UserProfileUpdateView(UpdateView):
    form_class = CustomUserChangeForm
    model = User
    template_name = 'users/edit.html'
    queryset = User.objects.all()
    success_url = reverse_lazy('dishes:dishes-list')

    def get_object(self, queryset=None):
        pk = self.kwargs.get(self.pk_url_kwarg)
        if pk == self.request.user.id:
            return self.request.user

        raise AttributeError("You cannot edit this profile!")


class UserProfileView(DetailView):
    model = User
    template_name = 'users/profile.html'
    context_object_name = 'user'
    queryset = User.objects.all()
