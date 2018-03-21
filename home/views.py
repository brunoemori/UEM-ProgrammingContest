from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from wiki.models import Article

#@login_required()
def home(request):
    return render(request, 'home/home.html', {"user": request.user})

def logout_view(request):
    if (request.user.is_authenticated):
        request.user.isUserOnline = False
        request.user.save()
        logout(request)

    return redirect('/home')
