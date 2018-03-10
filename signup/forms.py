from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=64, required=True,
        widget=forms.TextInput(attrs={'placeholder': 'First Name'}), label='')

    last_name = forms.CharField(max_length=64, required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Last Name'}), label='')

    username = forms.CharField(max_length=64, required=True, 
        widget=forms.TextInput(attrs={'placeholder': "Username (identification)"}), label='',
        error_messages={'': 'Username already used.'})

    email = forms.EmailField(max_length=32, required=True,
        widget=forms.TextInput(attrs={'placeholder': "Email"}), label='')

    avatar = forms.ImageField(required=False, help_text='Profile picture (optional)')
    
    password1 = forms.CharField(max_length=16, 
        widget=forms.PasswordInput(attrs={'placeholder': 'Password'}), label='')

    password2 = forms.CharField(max_length=16,
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirm password'}), label='')
 
    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2', 'avatar')

    def clean_image(self):
        image = self.cleaned_data.get('avatar')
        if (image):
            if (image._size > 2 * 1024 * 1024):
                raise forms.ValidationError('Image too large (> 4MB).')

            return image

        else:
            print('No image')
            return None
