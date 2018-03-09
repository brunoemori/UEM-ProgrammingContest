from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
import os

class UserManager(BaseUserManager):
    def createUser(self, email, password, username, **extraFields):
        if (not email):
            raise ValueError("User must have an email address.")

        if (not password):
            raise ValueError("User must have a password.")

        if (not username):
            raise ValueError('User must have an username')
        
        email = self.normalize_email(email)
        userObj = self.model(email=email, username=username, **extraFields)
        userObj.set_password(password)
        userObj.save(using=self._db)

        return userObj

    def create_user(self, email, password, username, **extraFields):
        return self.createUser(email, password, username, **extraFields)

    def create_superuser(self, email, password, username, **extraFields):
        extraFields.setdefault('is_superuser', True)
        extraFields.setdefault('is_staff', True)

        return self.createUser(email, password, username, **extraFields)

def get_avatar_path(instance, filename):
    return os.path.join('static/profile_pics/' + str(instance.id), filename)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    firstName = models.CharField(max_length=64)
    lastName = models.CharField(max_length=64)
    username = models.CharField(max_length=32, unique=True)
    bio = models.CharField(max_length=128, blank=True)
    email = models.EmailField(max_length=128, unique=True)
    isUserOnline = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    numArticles = models.PositiveIntegerField(default=0)
    dateJoined = models.DateTimeField(auto_now_add=True)
    avatar = models.ImageField(blank=True, upload_to=get_avatar_path, default='static/profile_pics/default.jpeg')

    USERNAME_FIELD = 'email'

    #Needed for creating superuser.
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def save(self, *args, **kwargs):
        if (self.id == None):
            img = self.avatar
            self.avatar = None
            super(CustomUser, self).save(*args, **kwargs)
            self.avatar = img

        super(CustomUser, self).save(*args, **kwargs)

    def __str__(self):
        return self.username

    @property
    def isSuperuser(self):
        return self.is_superuser

    @property
    def isStaff(self):
        return self.is_staff
