from django import forms
from signup.models import CustomUser

class UserPrefsForm(forms.ModelForm):
    firstName = forms.CharField(max_length=64, required=False,
        widget=forms.TextInput(attrs={'placeholder': 'First name'}), label='')

    lastName = forms.CharField(max_length=64, required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Last name'}), label='')

    email = forms.CharField(max_length=32, required=False,
             widget=forms.TextInput(attrs={'placeholder': "Email"}), label='')
     
    avatar = forms.ImageField(required=False, help_text='Profile picture (optional)')

    useDefaultAvatar = forms.BooleanField(required=False, help_text='Use default profile image.',
            widget=forms.CheckboxInput(attrs={'style': 'width:auto; display: inline'}))

    password1 = forms.CharField(max_length=16, required=False,
        widget=forms.PasswordInput(attrs={'placeholder': 'Password'}), label='')
    
    password2 = forms.CharField(max_length=16, required=False,
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirm password'}), label='')

    bio = forms.CharField(max_length=128, required=False,
        widget=forms.Textarea(attrs={'placeholder': 'You bio (max 256 characters)'}), label='')

    class Meta:
        model = CustomUser
        fields = ('firstName', 'lastName', 'email', 'password1', 'password2', 'bio', 'avatar', 'useDefaultAvatar', )

    def clean(self):
        return self.cleaned_data
