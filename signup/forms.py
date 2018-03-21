from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=64,
        widget=forms.TextInput(attrs={'placeholder': 'First Name'}), label='')

    last_name = forms.CharField(max_length=64,
        widget=forms.TextInput(attrs={'placeholder': 'Last Name'}), label='')

    username = forms.CharField(max_length=64, 
        widget=forms.TextInput(attrs={'placeholder': "Username"}), label='')

    email = forms.CharField(max_length=32,
        widget=forms.TextInput(attrs={'placeholder': "Email"}), label='')

    avatar = forms.ImageField(required=False, help_text='Profile picture (optional)')
    
    password1 = forms.CharField(max_length=16, 
        widget=forms.PasswordInput(attrs={'placeholder': 'Password'}), label='')

    password2 = forms.CharField(max_length=16,
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirm password'}), label='')
 
    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2', 'avatar',)

    def clean(self):
        cleanedData = self.cleaned_data
        if (cleanedData.get('first_name') == None):
            forms.ValidationError('\'First Name\' field cannot be empty')

        if (cleanedData.get('last_name') == None):
            forms.ValidationError('\'Last Name\' field cannot be empty')

        if (CustomUser.objects.all().filter(username=cleanedData.get('username'))):
            raise forms.ValidationError('Username already in use.')

        if (cleanedData.get('password1') != cleanedData.get('password2')):
            raise forms.ValidationError('Passwords don\'t match')

        if (len(cleanedData.get('password1')) < 8):
            raise forms.ValidationError('Password must have at least 8 characters')

        image = cleanedData.get('avatar')
        if (image):
            if (image._size > 2 * 1024 * 1024):
                raise forms.ValidationError('Image too large (> 2MB).')

        return cleanedData
