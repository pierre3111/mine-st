from django.shortcuts import render
from .models import Speaker

def all_speakers(request):
    speakers = Speaker.objects.all()
    return render(request, 'conferences/speakers.html', {'speakers': speakers})
