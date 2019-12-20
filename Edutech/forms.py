from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class SignUpForm(UserCreationForm):
    COUNTRY_CHOICES = [
    ('Kenya', 'Kenya'),
    ('Uganda', 'Uganda'),
    ('Tanzania', 'Tanzania'),
    ('Rwanda', 'Rwanda'),
    ]

    country = forms.CharField(label='Choose your country', widget=forms.Select(choices=COUNTRY_CHOICES ))
    email = forms.EmailField(max_length=200)

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2','email' )



class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio', 'age','interests',)