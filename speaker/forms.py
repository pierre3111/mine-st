from django import forms
from .models import Speaker

class SpeakerForm(forms.ModelForm):
    class Meta:
        model = Speaker
        fields = ['name', 'bio', 'contact_info', 'areas_of_expertise', 'profile_picture']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Customize form widgets or add additional form logic here if needed
