from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.template import loader
from .forms import UserLoginForm

from .services import *

def login(request):
    form = UserLoginForm(request.POST or None)

    if (form.is_valid()):
        usern = form.cleaned_data.get('username')
        passw = form.cleaned_data.get('password')

        authenticateUser(usern, passw, request)

        return redirect('/home')

    else:
        return render(request, 'login/login.html', {'form': form})
