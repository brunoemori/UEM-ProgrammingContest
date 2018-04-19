from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from signup.models import CustomUser
from .forms import UserPrefsForm

@login_required()
def userPreferences(request):
    user = CustomUser.objects.get(id=request.user.id)
    form = UserPrefsForm(request.POST, request.FILES)

    if (request.method == 'POST'):
        if (form.is_valid()):
            cleanedData = form.cleaned_data
            firstName = cleanedData.get('firstName')
            lastName = cleanedData.get('lastName')
            email = cleanedData.get('email')
            bio = cleanedData.get('bio')
            #avatar = cleanedData.get('avatar')
            useDefault = cleanedData.get('useDefaultAvatar')
            passw1 = cleanedData.get('password1')
            passw2 = cleanedData.get('password2')

            if (firstName != ''):
                if (len(firstName) > 64):
                    messages.error(request, 'First name must have less than 64 characters.')
                    return redirect('/prefs')
                else:
                    user.firstName = firstName

            if (lastName != ''):
                if (len(lastName) > 64):
                    messages.error(request, 'Last name must have less than 64 characters.')
                    return redirect('/prefs')
                else:
                    user.lastName = lastName

            if (email != ''):
                try:
                    validate_email(email)
                except ValidationError:
                    messages.error(request, 'Email not valid')
                    return redirect('/prefs')

                user.email = email

            if (bio != ''):
                if (len(bio) > 128):
                    messages.error(request, 'Your bio must have less than 128 characters')
                    return redirect('/prefs')
                else:
                    user.bio = bio
            
            '''
            if (avatar):
                if (avatar._size > 2 * 1024 * 1024):
                    messages.error(request, 'Image too large (> 2MB)')
                    return redirect('/prefs')
                else:
                    user.avatar = request.FILES['avatar']

            if (useDefault):
                user.avatar = CustomUser._meta.get_field('avatar').get_default()
            '''

            if (passw1 != ''):
                if (len(passw1) < 8):
                    messages.error(request, 'Password must have at least 8 characters')
                    return redirect('/prefs')
                elif (passw1 != passw2):
                    messages.error(request, 'Passwords don\'t match')
                    return redirect('/prefs')
                else:
                    user.set_password(passw1)

            user.save()
            messages.success(request, 'Preferences saved.')

        else:
            form = UserPrefsForm()

    return render(request, 'preferences/prefs.html', {'form': form})
    
