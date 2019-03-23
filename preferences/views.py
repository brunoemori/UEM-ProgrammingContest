from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from signup.models import CustomUser
from .forms import UserPrefsForm
from signup import services

@login_required()
def userPreferences(request):
    user = CustomUser.objects.get(id=request.user.id)
    form = UserPrefsForm(request.POST, request.FILES)

    if (request.method == 'POST'):
        if (form.is_valid(request)):
            services.editUser(user, form)
            messages.success(request, 'Preferences saved!')
            return redirect('/prefs')

        else:
            form = UserPrefsForm()

    return render(request, 'preferences/prefs.html', {'form': form})
    
