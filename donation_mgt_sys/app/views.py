from django.shortcuts import render
from .models import FeedbackModel, AboutModel, ServiceModel, GalleryModel

# Create your views here.
def home(request):
    feedback = FeedbackModel.objects.all()
    print(feedback)
    return render(request, 'base.html', {'feedback': feedback})

def about(request):
    about = AboutModel.objects.all()
    return render(request, 'about.html', {'about': about})

def services(request):
    service = ServiceModel.objects.all()
    return render(request, 'service.html', {'service': service})

def gallery(request):
    gallery = GalleryModel.objects.all()
    return render(request, 'gallery.html', {'gallery': gallery})

def event(request):
    return render(request, 'event.html')

def team(request):
    return render(request, 'team.html')

def donate(request):
    return render(request, 'donate.html')

def contact(request):
    return render(request, 'contact.html')
