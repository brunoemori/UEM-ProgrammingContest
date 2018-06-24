from django import forms
from django.contrib.auth import authenticate, get_user_model

User = get_user_model()

class UserLoginForm(forms.Form):
    username = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Usuário'}))
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': 'Senha'}))

    def clean(self, *args, **kwargs):
        usern = self.cleaned_data.get('username')
        passw = self.cleaned_data.get('password')

        if (usern and passw):
            user = authenticate(username=usern, password=passw)

            if (not user):
                raise forms.ValidationError('Wrong username or password.')

            if (not user.check_password(passw)):
                raise forms.ValidationError('Wrong usernamej or password.')

            if (not user.is_active):
                raise forms.ValidationError('This user is no longer active.')

            return super(UserLoginForm, self).clean(*args, **kwargs)
