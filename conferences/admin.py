from django.contrib import admin
from .models import Conference

@admin.register(Conference)
class ConferenceAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'date', 'venue', 'theme')
    list_filter = ('category',)
    search_fields = ('name', 'category', 'venue', 'theme')
