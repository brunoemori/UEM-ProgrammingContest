from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .forms import SignUpForm
from .models import CustomUser

def signup(request):
    if (request.method == 'POST'):
        form = SignUpForm(request.POST, request.FILES)
        if (form.is_valid()):
            print('FORM VALID')
            user = CustomUser()

            cleanedData = form.cleaned_data
            username = cleanedData.get('username')
            email = cleanedData.get('email')
            passw1 = cleanedData.get('password1')
            passw2 = cleanedData.get('password2')
            firstName = cleanedData.get('firstName')
            lastName = cleanedData.get('lastName')
            avatar = cleanedData.get('avatar')

            if (username == ''):
                messages.error(request, 'Username cannot be empty.')
            elif (len(username) > 32):
                messages.error(request, 'Username must have less than 32 characters.')
            else:
                user.username = username

            if (len(passw1) < 8):
                messages.error(request, 'Password must have at least 8 characters')
            else:
                if (passw1 != passw2):
                    messages.error(request, 'Passwords don\'t match.')
                
            if (firstName == ''):
                messages.error(request, 'First name cannot be empty.')
            elif (len(firstName) > 64):
                messages.error(request, 'First name must have less than 64 characters.')
            else:
                user.firstName = firstName

            if (lastName == ''):
                messages.error(request, 'Last name cannot be empty.')
            elif (len(lastName) > 64):
                messages.error(request, 'Last name must have less than 64 characters.')
            else:
                user.lastName = lastName

            if (email != ''):
                try:
                    validate_email(email)
                except ValidationError:
                    messages.error(request, 'Email not valid')

                user.email = email

            if (avatar):
                if (avatar.size > 2 * 1024 * 1024):
                    messages.error(request, 'Image too large (> 2MB)')
                else:
                    user.avatar = request.FILES['avatar'].read()

            errorMsgs = messages.get_messages(request)

            if (len(errorMsgs) >= 1):
                return redirect('/signup')
            else:
                user.save()
                return redirect('/')

                
    else:
        form = SignUpForm()

    return render(request, 'signup/register.html', {'form' : form})
