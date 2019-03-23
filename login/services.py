from django.contrib.auth import authenticate

def authenticateUser(usern, passw, request):
    user = authenticate(username=usern, password=passw)

    if user is not None:
        user.isUserOnline = True
        user.save()

    return user