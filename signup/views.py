from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from .forms import SignUpForm
from login.services import authenticateUser

from .services import *


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid(request):
            user = createUser(request, form)
            authenticateUser(form.cleaned_data['username'], form.cleaned_data['password1'], request)
            auth_login(request, user)
            return redirect('/home')

    else:
        form = SignUpForm()

    return render(request, 'signup/register.html', {'form': form})
