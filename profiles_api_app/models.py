from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
# Create your models here.


class UserProfileManager(BaseUserManager):
    """
    UserProfileManager is the class that would help to interface with the django cli
    """
    def create_user(self, email, name, password=None):
        """
        Create New User Profile
        """
        print("FirstTime: "+str(name))
        if not email:
            raise ValueError('Email has not been provided')

        #normalize_email is simply a method that shall lowercase the @<domain> to avoid any amiguities
        email = self.normalize_email(email)
        name = name
        print("SecondTime: "+str(name))
        user = self.model(email=email, name=name)
        user.set_password(password)

        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password=None):
        """
        Create a superuser
        """
        user = self.create_user(email, name, password)
        user.is_staff = True
        user.is_superuser = True

        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """
    UserProfile is the application replacement for the default user model.
    """
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """
        Returns the name.
        """
        return self.name

    def get_short_name(self):
        """
        Returns the name.
        """
        return self.name

    def __str__(self):
        """
        Returns the string representation email
        """
        return self.email
