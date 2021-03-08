from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('apps.dishes.urls', 'dishes'), namespace='dishes')),
    path('tables/', include(('apps.tables.urls', 'tables'), namespace='tables')),
    path('reservations/', include(('apps.reservations.urls', 'reservations'), namespace='reservations')),
    path('', include(('apps.users.urls', 'users'), namespace='users')),
    path('accounts/', include('allauth.urls')),
    # path('', TemplateView.as_view(template_name='home.html'), name='home'),
]

# for serving uploaded files on dev environment with django
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT
    )
