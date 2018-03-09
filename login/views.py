from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.template import loader
from .forms import UserLoginForm

def login(request):
    form = UserLoginForm(request.POST or None)

    if (form.is_valid()):
        email = form.cleaned_data.get('email')
        passw = form.cleaned_data.get('password')

        user = authenticate(username=email, password=passw)
        auth_login(request, user)
        user.isUserOnline = True
        user.save()

        print("User " + user.firstName + " " + user.lastName + " logged in")
        return redirect('/home/')
    
    return render(request, 'login/login.html', {'form': form})
