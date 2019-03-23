from django.contrib.auth import authenticate

def authenticateUser(usern, passw, request):
    user = authenticate(username=usern, password=passw)
    user.isUserOnline = True
    user.save()