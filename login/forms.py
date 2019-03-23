from django import forms
from django.contrib.auth import authenticate, get_user_model
from django.contrib import messages

User = get_user_model()

class UserLoginForm(forms.Form):
    username = forms.CharField(required=False, label='', widget=forms.TextInput(attrs={'placeholder': 'Usuário'}))
    password = forms.CharField(required=False, label='', widget=forms.PasswordInput(attrs={'placeholder': 'Senha'}))

    class Meta:
        fields = ('username', 'password', )

    def is_valid(self, request):
        super(UserLoginForm, self).is_valid()

        data = self.cleaned_data

        usern = data['username']
        passw = data['password']

        if usern and passw:
            user = authenticate(username=usern, password=passw)

            if not user:
                messages.error(request, 'Wrong username of password')

            elif not user.check_password(passw):
                messages.error(request, 'Wrong username or password.')

            elif not user.is_active:
                messages.error(request, 'This user is no longer active.')

            return True

        else:
            messages.error(request, 'Please input your credentials.')

        return False