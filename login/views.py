from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from .forms import UserLoginForm

from .services import *

def login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST or None)

        if (form.is_valid(request)):
            data = form.cleaned_data

            usern = data['username']
            passw = data['password']

            user = authenticateUser(usern, passw, request)

            if (user is not None):
                auth_login(request, user)
                return redirect('/home')
            else:
                return redirect('/login')

    else:
        form = UserLoginForm()

    return render(request, 'login/login.html', {'form': form})
