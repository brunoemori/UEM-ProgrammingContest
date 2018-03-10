from django import forms
from django.contrib.auth import authenticate, get_user_model

User = get_user_model()

class UserLoginForm(forms.Form):
    email = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

    def clean(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        passw = self.cleaned_data.get('password')

        if (email and passw):
            user = authenticate(username=email, password=passw)

            if (not user):
                raise forms.ValidationError('Wrong email or password.')

            if (not user.check_password(passw)):
                raise forms.ValidationError('Wrong email or password.')

            if (not user.is_active):
                raise forms.ValidationError('This user is no longer active.')

            return super(UserLoginForm, self).clean(*args, **kwargs)
