from django.contrib import admin
from .models import Registration

@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'job_role', 'conference')
    list_filter = ('job_role', 'conference')
    search_fields = ('name', 'email', 'job_role', 'topics_interest')
    # Additional options or customization can be added here
