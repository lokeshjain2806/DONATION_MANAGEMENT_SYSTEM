# Generated by Django 5.0.1 on 2024-02-05 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='about_images/', verbose_name='About Image')),
                ('name', models.CharField(max_length=150, verbose_name='Name')),
                ('description', models.TextField()),
                ('created_at', models.DateField(auto_now=True)),
                ('updated_at', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='BlogModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='blog_images/', verbose_name='Blog Image')),
                ('title', models.CharField(max_length=150, verbose_name='Title')),
                ('about', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('created_at', models.DateField(auto_now=True)),
                ('updated_at', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ContactModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Name')),
                ('email', models.EmailField(max_length=254, verbose_name='Email Id')),
                ('message', models.TextField()),
                ('created_at', models.DateField(auto_now=True)),
                ('updated_at', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='EventsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='event_images/', verbose_name='Event Image')),
                ('title', models.CharField(max_length=150, verbose_name='Title')),
                ('description', models.TextField()),
                ('created_at', models.DateField(auto_now=True)),
                ('updated_at', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='FeedbackModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='feedback_images/', verbose_name='Feedback Image')),
                ('name', models.CharField(max_length=150, verbose_name='Name')),
                ('feedback', models.TextField()),
                ('created_at', models.DateField(auto_now=True)),
                ('updated_at', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='GalleryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='gallery_images/', verbose_name='Gallery Image')),
                ('title', models.CharField(max_length=150, verbose_name='Title')),
                ('about', models.TextField()),
                ('created_at', models.DateField(auto_now=True)),
                ('updated_at', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ServiceModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='service_images/', verbose_name='Service Image')),
                ('title', models.CharField(max_length=150, verbose_name='Title')),
                ('description', models.TextField()),
                ('created_at', models.DateField(auto_now=True)),
                ('updated_at', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TeamModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='team_images/', verbose_name='Team Image')),
                ('name', models.CharField(max_length=150, verbose_name='Name')),
                ('post', models.CharField(max_length=150, verbose_name='Post Name')),
                ('description', models.TextField()),
                ('twitter', models.CharField(max_length=150, verbose_name='Twitter')),
                ('facebook', models.CharField(max_length=150, verbose_name='Facebook')),
                ('gmail', models.CharField(max_length=150, verbose_name='Gmail')),
                ('linkdin', models.CharField(max_length=150, verbose_name='Linkdin')),
                ('created_at', models.DateField(auto_now=True)),
                ('updated_at', models.DateField(blank=True, null=True)),
            ],
        ),
    ]