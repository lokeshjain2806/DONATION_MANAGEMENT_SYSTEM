from django.db import models
from PIL import Image


# Create your models here.
class BlogModel(models.Model):
    image = models.ImageField(upload_to='blog_images/', verbose_name='Blog Image')
    title = models.CharField(max_length=150, verbose_name='Title')
    about = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateField(auto_now=True)
    updated_at = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title


class AboutModel(models.Model):
    image = models.ImageField(upload_to='about_images/', verbose_name='About Image')
    name = models.CharField(max_length=150, verbose_name='Name')
    description = models.TextField()
    created_at = models.DateField(auto_now=True)
    updated_at = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name


class ServiceModel(models.Model):
    image = models.ImageField(upload_to='service_images/', verbose_name='Service Image')
    title = models.CharField(max_length=150, verbose_name='Title')
    description = models.TextField()
    created_at = models.DateField(auto_now=True)
    updated_at = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title


class FeedbackModel(models.Model):
    image = models.ImageField(upload_to='feedback_images/', verbose_name='Feedback Image')
    name = models.CharField(max_length=150, verbose_name='Name')
    feedback = models.TextField()
    created_at = models.DateField(auto_now=True)
    updated_at = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name


class EventsModel(models.Model):
    image = models.ImageField(upload_to='event_images/', verbose_name='Event Image')
    title = models.CharField(max_length=150, verbose_name='Title')
    description = models.TextField()
    created_at = models.DateField(auto_now=True)
    updated_at = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title


class GalleryModel(models.Model):
    image = models.ImageField(upload_to='gallery_images/', verbose_name='Gallery Image')
    title = models.CharField(max_length=150, verbose_name='Title')
    about = models.TextField()
    created_at = models.DateField(auto_now=True)
    updated_at = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title

class TeamModel(models.Model):
    image = models.ImageField(upload_to='team_images/', verbose_name='Team Image')
    name = models.CharField(max_length=150, verbose_name='Name')
    post = models.CharField(max_length=150, verbose_name='Post Name')
    description = models.TextField()
    twitter = models.CharField(max_length=150, verbose_name='Twitter')
    facebook = models.CharField(max_length=150, verbose_name='Facebook')
    gmail = models.CharField(max_length=150, verbose_name='Gmail')
    linkdin = models.CharField(max_length=150, verbose_name='Linkdin')
    created_at = models.DateField(auto_now=True)
    updated_at = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name


class ContactModel(models.Model):
    name = models.CharField(max_length=150, verbose_name='Name')
    email = models.EmailField(verbose_name='Email Id')
    message = models.TextField()
    created_at = models.DateField(auto_now=True)
    updated_at = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name
