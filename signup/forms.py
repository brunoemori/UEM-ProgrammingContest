from django import forms
from django.contrib import messages
from .services import *
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.shortcuts import redirect

class SignUpForm(forms.Form):
    firstName = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'First Name'}), label='')

    lastName = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Last Name'}), label='')

    username = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': "Username"}), label='')

    email = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': "Email"}), label='')

    avatar = forms.ImageField(required=False, help_text='Profile picture (optional)')

    password1 = forms.CharField(required=False, widget=forms.PasswordInput(attrs={'placeholder': 'Password'}), label='')

    password2 = forms.CharField(required=False, widget=forms.PasswordInput(attrs={'placeholder': 'Confirm password'}),

                                label='')

    class Meta:
        fields = ('firstName', 'lastName', 'username', 'email', 'password1', 'password2', 'avatar',)

    def is_valid(self, request):
        super(SignUpForm, self).is_valid()

        data = self.cleaned_data

        if data['username'] == '':
            messages.error(request, 'Username cannot be empty.')
        elif len(data['username']) > 32:
            messages.error(request, 'Username must have less than 32 characters.')
        elif checkUsernameExists(data['username']):
            messages.error(request, 'Username already in use.')

        if len(data['password1']) < 8:
            messages.error(request, 'Password must have at least 8 characters')
        elif data['password1'] != data['password2']:
            messages.error(request, 'Passwords don\'t match.')

        if data['firstName'] == '':
            messages.error(request, 'First name cannot be empty.')
        elif len(data['firstName']) > 64:
            messages.error(request, 'First name must have less than 64 characters.')

        if data['lastName'] == '':
            messages.error(request, 'Last name cannot be empty.')
        elif len(data['lastName']) > 64:
            messages.error(request, 'Last name must have less than 64 characters.')

        if data['email'] != '':
            try:
                validate_email(data['email'])
            except ValidationError:
                messages.error(request, 'Email not valid')

        if data['avatar']:
            if data['avatar'].size > 2 * 1024 * 1024:
                messages.error(request, 'Image too large (> 2MB)')

        errorMsgs = messages.get_messages(request)

        if len(errorMsgs) >= 1:
            return False

        return True

