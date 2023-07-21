# project_name/conference_management_system/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # Add the URL patterns for the 'conferences' app
    path('', include('conferences.urls')),
    # Add the URL patterns for the 'speaker' app
    path('speaker/', include('speaker.urls')),
    # Add the URL patterns for the 'registration' app
    path('registration/', include('registration.urls')),
]

# Add the following line at the end of the urlpatterns list
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
