from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'base.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'service.html')

def gallery(request):
    return render(request, 'gallery.html')

def event(request):
    return render(request, 'event.html')

def team(request):
    return render(request, 'team.html')

def donate(request):
    return render(request, 'donate.html')

def contact(request):
    return render(request, 'contact.html')
