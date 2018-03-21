from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import SignUpForm

def signup(request):
    if (request.method == 'POST'):
        form = SignUpForm(request.POST, request.FILES)
        if (form.is_valid()):
            user = form.save(commit=False)
            user.firstName = form.cleaned_data.get('first_name')
            user.lastName = form.cleaned_data.get('last_name')
            
            image = form.cleaned_data.get('avatar')
                
            if (image):
                user.avatar = request.FILES['avatar']
    
            user.save()
                
            return redirect('/')
    else:
        form = SignUpForm()

    print(form.errors)
    return render(request, 'signup/register.html', {'form' : form})
