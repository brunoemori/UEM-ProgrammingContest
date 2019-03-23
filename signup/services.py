from signup.models import CustomUser

def checkUsernameExists(username):
    try:
        CustomUser.objects.get(username=username)
    except CustomUser.DoesNotExist:
        return False

    return True

def createUser(request, form):
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

