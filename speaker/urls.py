from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_speakers, name='all_speakers'),
    # Add any additional speaker-related URLs here if needed
]
