from django.urls import path
from . import views

urlpatterns = [
    path('', views.registration_form, name='registration'),
    path('registration/success/', views.registration_success, name='registration_success'),

]

