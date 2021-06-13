# from django.shortcuts import render, redirect
# from django import forms
# from django.contrib.auth.models import User
# from .forms import *
# from django.contrib.auth import login, authenticate
# def signup(request):
#     if request.method == 'POST':
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             raw_password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=raw_password)
#             login(request, user)
#             return redirect('homepage')
#     else:
#         form = SignUpForm()
#     return render(request, 'registration/signup.html', {'form': form})
from django.shortcuts import render, redirect
from .models import Profile
# from .forms import CustomUserCreationForm
from django.contrib import messages
from django import forms
from django.contrib.auth.models import User
from .forms import *
from django.contrib.auth import login, authenticate
# Create your views here.

def signup(request):
    if request.user.is_superuser:
        messages.error(request, 'You are already signed up and logged in!!')
        return redirect('all_customers')

    form = CustomUserCreationForm()

    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user)
            messages.success(request, 'Account created successfully')
            return redirect('login')
        else:
            messages.error(request, 'there was a problem with your signup data, please try again')
    return render(request, 'registration/signup.html', {'signupform':form})