import os
from django.shortcuts import render, get_object_or_404
from .models import Conference, Speaker


def home(request):
    conferences = Conference.objects.all()
    return render(request, 'conferences/home.html', {'conferences': conferences})


def about(request):
    return render(request, 'conferences/about.html')

def speakers(request):
    speakers = Speaker.objects.all()
    return render(request, 'conferences/speakers.html', {'speakers': speakers})

def schedule(request):
    return render(request, 'conferences/schedule.html')

def conference_detail(request, conference_id):
    conference = get_object_or_404(Conference, pk=conference_id)
    return render(request, 'conferences/conference_detail.html', {'conference': conference})
