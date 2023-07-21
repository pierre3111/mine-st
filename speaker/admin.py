# speaker/admin.py
from django.contrib import admin
from .models import Speaker

class SpeakerAdmin(admin.ModelAdmin):
    list_display = ('name', 'website', 'twitter_handle')
    search_fields = ('name', 'bio')
    list_filter = ('website',)

admin.site.register(Speaker, SpeakerAdmin)
