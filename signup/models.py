from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from PIL import Image
from pcwiki import const

import io


class UserManager(BaseUserManager):
    def createUser(self, email, password, username, **extraFields):
        if not password:
            raise ValueError("User must have a password.")

        if not username:
            raise ValueError('User must have an username')

        if len(username) < const.USER_USERNAME_MINLENGTH:
            raise ValueError('Username must have at least' + const.USER_USERNAME_MINLENGTH + 'characters.')
        
        if (email):
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

def defaultAvatar():
    with open(const.PROFILE_PICS_PATH + const.DEFAULT_PROFILE_PIC, 'rb') as f:
        return bytearray(f.read())

class CustomUser(AbstractBaseUser, PermissionsMixin):
    firstName = models.CharField(max_length=const.USER_FIRSTNAME_MAXLENGTH, blank=False)
    lastName = models.CharField(max_length=const.USER_LASTNAME_MAXLENGTH, blank=False)
    username = models.CharField(max_length=const.USER_USERNAME_MAXLENGTH, unique=True)
    bio = models.CharField(max_length=const.USER_BIO_MAXLENGHT, blank=True)
    email = models.EmailField(max_length=const.USER_EMAIL_MAXLENGTH, default='')
    isUserOnline = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    numArticles = models.PositiveIntegerField(default=0)
    dateJoined = models.DateTimeField(auto_now_add=True)
    avatar = models.BinaryField(max_length=const.USER_AVATAR_MAXSIZE, blank=True, null=True,
                                 default=defaultAvatar, editable=True)

    USERNAME_FIELD = 'username'

    #Needed for creating superuser.
    REQUIRED_FIELDS = ['email']

    objects = UserManager()

    def save(self, *args, **kwargs):
        if self.id is None:
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

    def getAvatarImage(self):
        if self.avatar is not None:
            avatar = Image.open(io.BytesIO(self.avatar))
            with open(const.PROFILE_PICS_PATH + const.DEFAULT_PROFILE_PIC, 'rb') as f:
                if avatar == f.read():
                    imgPath = const.PROFILE_PICS_PATH + const.DEFAULT_PROFILE_PIC
                else:
                    imgPath = const.PROFILE_PICS_PATH + str(self.id) + '.png'
                    avatar.save(imgPath)
    
            return imgPath
