from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('speakers/', views.speakers, name='speakers'),
    path('schedule/', views.schedule, name='schedule'),
    path('conference/<int:conference_id>/', views.conference_detail, name='conference_detail'),
]
