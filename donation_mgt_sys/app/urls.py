"""
URL configuration for donation_mgt_sys project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import Home, about, services, gallery, event, team, Login, Contact, Blog, RegistrationView

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('about/', about, name='about'),
    path('services/', services, name='services'),
    path('gallery/', gallery, name='gallery'),
    path('event/', event, name='event'),
    path('team/', team, name='team'),
    path('sign_in/', Login.as_view(), name='login'),
    path('contact/', Contact.as_view(), name='contact'),
    path('blog/<int:id>/', Blog.as_view(), name='blogdetails'),
    path('registration/', RegistrationView.as_view(), name='registration'),

]
