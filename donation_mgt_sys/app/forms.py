from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import MyUser

class RegistrationForm(UserCreationForm):
    type = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices=MyUser.REGISTRATION_CHOICES,
    )

    class Meta:
        model = MyUser
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

        self.fields['username'].help_text = ''
        self.fields['password1'].help_text = ''
        self.fields['password2'].help_text = ''


class LoginForm(forms.Form):
    username = forms.CharField(label='Username',
                                widget=forms.TextInput(attrs={'class': 'form-control'})
                                )
    password = forms.CharField(label='Password',
                               widget=forms.PasswordInput(attrs={'class': 'form-control'})
                               )

    class Meta:
        model = MyUser
        fields = ['username', 'password']


class LoginOtpForm(forms.Form):
    username = forms.CharField(label='Username',
                               widget=forms.TextInput(attrs={'class': 'form-control'}))


class OtpVerificationForm(forms.Form):
    otp = forms.IntegerField(label='Enter Your Otp', widget=forms.TextInput(attrs={'class': 'form-control'}))
