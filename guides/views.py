from django.shortcuts import render

def home(request):
    return render(request, 'guides/home.html')

def n1(request):
    return render(request, 'guides/n1.html')

def n2(request):
    return render(request, 'guides/n2.html')

def n3(request):
    return render(request, 'guides/n3.html')
