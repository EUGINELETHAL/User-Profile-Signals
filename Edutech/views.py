from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .forms import *
from.models import *
from django.db import transaction
from django.contrib import messages
from django.utils.translation import gettext as _

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            email =form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/update')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, _('Your profile was successfully updated!'))
            return redirect('/home')
        else:
            messages.error(request, _('Please correct the error below.'))
    else:
        user_form = UserCreationForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })


def home (request):
    return render(request, 'home.html')

def profile(request):
    return render(request, 'profile.html')