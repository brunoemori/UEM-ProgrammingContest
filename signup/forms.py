from django import forms
from .models import CustomUser

class SignUpForm(forms.ModelForm):
    firstName = forms.CharField(max_length=64, required=False,
        widget=forms.TextInput(attrs={'placeholder': 'First Name'}), label='')

    lastName = forms.CharField(max_length=64, required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Last Name'}), label='')

    username = forms.CharField(max_length=64, required=False,
        widget=forms.TextInput(attrs={'placeholder': "Username"}), label='')

    email = forms.CharField(max_length=32, required=False,
        widget=forms.TextInput(attrs={'placeholder': "Email"}), label='')

    avatar = forms.ImageField(required=False, help_text='Profile picture (optional)')
    
    password1 = forms.CharField(max_length=16, required=False,
        widget=forms.PasswordInput(attrs={'placeholder': 'Password'}), label='')

    password2 = forms.CharField(max_length=16, required=False,
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirm password'}), label='')
 
    class Meta:
        model = CustomUser
        fields = ('firstName', 'lastName', 'username', 'email', 'password1', 'password2', 'avatar',)

    def clean(self):
        return self.cleaned_data

