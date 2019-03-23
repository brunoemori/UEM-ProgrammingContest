from django import forms
from pcwiki import const
from django.contrib import messages
from django.core.validators import validate_email
from django.core.exceptions import ValidationError


class UserPrefsForm(forms.Form):
    firstName = forms.CharField(required=False,
        widget=forms.TextInput(attrs={'placeholder': 'First name'}), label='')

    lastName = forms.CharField(required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Last name'}), label='')

    email = forms.CharField(required=False,
             widget=forms.TextInput(attrs={'placeholder': "Email"}), label='')
     
    avatar = forms.ImageField(required=False, help_text='Profile picture (optional)')

    useDefaultAvatar = forms.BooleanField(required=False, help_text='Use default profile image.',
            widget=forms.CheckboxInput(attrs={'style': 'width:auto; display: inline'}))

    password1 = forms.CharField(required=False,
        widget=forms.PasswordInput(attrs={'placeholder': 'Password'}), label='')
    
    password2 = forms.CharField(required=False,
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirm password'}), label='')

    bio = forms.CharField(required=False,
        widget=forms.Textarea(attrs={'placeholder': 'You bio (max ' + str(const.USER_BIO_MAXLENGHT) + ' characters)'}),
                          label='')

    class Meta:
        fields = ('firstName', 'lastName', 'email', 'password1', 'password2', 'bio', 'avatar', 'useDefaultAvatar', )

    def clean(self):
        return self.cleaned_data

    def is_valid(self, request):
        super(UserPrefsForm, self).is_valid()

        data = self.cleaned_data

        if data['firstName']:
            if len(data['firstName']) > const.USER_FIRSTNAME_MAXLENGTH:
                messages.error(request, 'First name must have less than ' + str(const.USER_FIRSTNAME_MAXLENGTH)
                               + ' characters.')

        if data['lastName']:
            if len(data['lastName']) > const.USER_LASTNAME_MAXLENGTH:
                messages.error(request, 'Last name must have less than ' + str(const.USER_LASTNAME_MAXLENGTH)
                               + ' characters.')

        if data['email']:
            if len(data['email']) > const.USER_EMAIL_MAXLENGTH:
                messages.error(request, 'Last name must have less than '
                               + str(const.USER_EMAIL_MAXLENGTH) + ' characters.')
            else:
                try:
                    validate_email(data['email'])
                except ValidationError:
                    messages.error(request, 'Email not valid')

        if not data['useDefaultAvatar']:
            if data['avatar']:
                if data['avatar'].size > const.USER_AVATAR_MAXSIZE:
                    messages.error(request, 'Image too large (> ' + str(const.USER_AVATAR_MAXSIZE) + ')')

        if data['bio']:
            if len(data['bio']) > const.USER_BIO_MAXLENGHT:
                messages.error(request,
                               'Your bio must have less than ' + str(const.USER_BIO_MAXLENGHT) + ' characters.')

        if data['password1']:
            if len(data['password1']) < const.USER_PASSW_MINLENGTH:
                messages.error(request,
                               'Your password must have at least ' + str(const.USER_PASSW_MINLENGTH) + ' character(s)')

            elif len(data['password1']) > const.USER_PASSW_MAXLENGTH:
                messages.error(request,
                               'Your password must have less than ' + str(const.USER_PASSW_MAXLENGTH) + ' character(s)')

            elif data['password1'] != data['password2']:
                messages.error(request, 'Passwords don\'t match.')

        errorMsgs = messages.get_messages(request)

        if len(errorMsgs) >= 1:
            return False

        return True