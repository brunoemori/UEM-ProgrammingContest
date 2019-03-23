from signup.models import CustomUser
from pcwiki import const

#User services

def checkUsernameExists(username):
    try:
        CustomUser.objects.get(username=username)
    except CustomUser.DoesNotExist:
        return False

    return True

def createUser(form):
    user = CustomUser()

    data = form.cleaned_data

    user.username = data['username']
    user.firstName = data['firstName']
    user.lastName = data['lastName']
    user.set_password(data['password1'])
    user.email = data['email']

    if data['avatar'] is not None:
        user.avatar = data['avatar'].read()

    user.save()

    return user

def editUser(user, form):
    data = form.cleaned_data

    if data['firstName']:
        user.firstName = data['firstName']

    if data['lastName']:
        user.lastName = data['lastName']

    if data['password1']:
        user.set_password(data['password1'])

    if data['email']:
        user.email = data['email']

    if data['bio']:
        user.bio = data['bio']

    if data['useDefaultAvatar']:
        with open(const.PROFILE_PICS_PATH + const.DEFAULT_PROFILE_PIC, 'rb') as f:
          user.avatar = f.read()

    elif data['avatar']:
        user.avatar = data['avatar']

    user.save()

    return user