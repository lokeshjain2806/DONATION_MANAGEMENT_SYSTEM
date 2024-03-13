from django.contrib.auth import authenticate, login
from django.contrib.auth.views import PasswordResetView
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from django.core.mail import send_mail
from .models import FeedbackModel, AboutModel, ServiceModel, GalleryModel, TeamModel, ContactModel, BlogModel, \
    SubscriptionModel, MyUser
from .forms import RegistrationForm, LoginForm, LoginOtpForm, OtpVerificationForm, SignUpFormDonor, VolunteerModelForm
from django.contrib import messages
import random


# Create your views here.
class Home(View):
    def get(self, request):
        feedback = FeedbackModel.objects.all()
        blogs = BlogModel.objects.all()
        return render(request, 'base.html', {'feedback': feedback, 'blogs': blogs})

    def post(self, request):
        feedback = FeedbackModel.objects.all()
        blogs = BlogModel.objects.all()
        email = request.POST.get('mail')
        subscription = SubscriptionModel(email=email)
        subscription.save()
        subject = 'Subscription Confirmation'
        message = 'Thank you for subscribing to our newsletter!'
        from_email = 'reset9546@gmail.com'
        to_email = [email]
        send_mail(subject, message, from_email, to_email)
        return render(request, 'base.html', {'feedback': feedback, 'blogs': blogs})

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
    teams = TeamModel.objects.all()
    return render(request, 'team.html', {'teams': teams})


class Login(View):
    def get(self, request):
        form = LoginForm
        return render(request, 'signin.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                a = user.is_completed
                login(request, user)
                if a is False:
                    return redirect('complete_profile')
                else:
                    login(request, user)
                    return HttpResponse("6666666666")
            else:
                messages.error(request, 'Username Or Password is invalid')
                return render(request, 'signin.html', {'form': form})
        else:
            return render(request, 'signin.html', {'form': form})


class Contact(View):
    def get(self, request):
        return render(request, 'contact.html')

    def post(self, request):
        name = request.POST.get('name')
        email = request.POST.get('mail')
        message = request.POST.get('message')
        contact = ContactModel(name=name, email=email, message=message)
        contact.save()
        subject = 'New Contact Form Submission'
        message = f'You have received a new contact form submission from {name}.\n Email: {email}.\n Message: {message}\n'
        from_email = 'reset9546@gmail.com'
        to_email = ['lokeshjain2806@gmail.com']
        send_mail(subject, message, from_email, to_email)
        return render(request, 'contact.html')

class Blog(View):
    def get(self, request, id):
        blogs = BlogModel.objects.filter(id=id)
        return render(request, 'blogdetails.html', {'blogs': blogs})


class RegistrationView(View):
    def get(self, request):
        form =RegistrationForm
        return render(request, 'registration.html', {'form': form})

    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            a = MyUser.objects.filter(email=email).exists()
            user_name = form.cleaned_data['username']
            b = MyUser.objects.filter(username=user_name).exists()
            if a:
                messages.error(request, 'Email is already exist')
                return render(request, 'registration.html', {'form': form})
            if b:
                messages.error(request, 'username is already exist')
                return render(request, 'registration.html', {'form': form})
            user = MyUser.objects.create_user(
                username=user_name,
                email=email,
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                password=form.cleaned_data['password1'],
                type=form.cleaned_data['type'],
            )
            return HttpResponse('home')
        else:
            return render(request, 'registration.html', {'form': form})


class OtpLogin(View):
    def get(self, request):
        form = LoginOtpForm
        return render(request, 'loginviaotp.html', {'form': form})

    def post(self, request):
        form = LoginOtpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            a = MyUser.objects.filter(username=username).exists()
            if a:
                user = MyUser.objects.get(username=username)
                num_numbers = 4
                random_numbers = []
                for i in range(num_numbers):
                    random_1_digit = random.randint(1, 9)
                    random_numbers.append(str(random_1_digit))
                otp = int(''.join(random_numbers))
                request.session['user'] = user.id
                request.session['expected_otp'] = otp
                request.session.save()
                print(otp)
                subject = 'Login Verification'
                message = f'Otp For Login: {otp}. Otp is valid for 10 minutes only.'
                from_email = 'reset9546@gmail.com'
                recipient_list = [user.email]
                fail_silently = False
                send_mail(subject, message, from_email, recipient_list, fail_silently)
                return redirect('otp_verification')


class OtpFun(View):
    def get(self, request):
        form = OtpVerificationForm
        return render(request, 'otpverification.html', {'form': form})

    def post(self, request):
        form = OtpVerificationForm(request.POST)
        entered_otp = request.POST.get('otp')
        expected_otp = request.session.get('expected_otp')
        user_id = request.session.get('user')
        user = MyUser.objects.get(id=user_id)
        if str(entered_otp) == str(expected_otp):
            login(request, user)
            return HttpResponse("55555555555555555")
        else:
            messages.error(request, 'OTP Not Valid')
            return render(request, 'otpverification.html', {'form': form})


class CustomPasswordResetView(PasswordResetView):
    def form_valid(self, form):
        try:
            email = form.cleaned_data['email']
            user = MyUser.objects.get(email=email)
        except ObjectDoesNotExist:
            messages.error(self.request, 'User with this email does not exist.')
            return redirect('password-reset')
        return super().form_valid(form)


class Complete_Profile(View):
    def get(self, request):
        if request.user.type == 'Is Volunteers':
            form = VolunteerModelForm
            return render(request, 'complete_profile.html', {'form': form})
        else:
            form = SignUpFormDonor
            return render(request, 'complete_profile.html', {'form': form})



