import email
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.hashers import make_password

# Create your models here.

class AccountManager(BaseUserManager):
    def create_user(self, username, fullname, email, password=None):
        if not email:
            raise ValueError("Users must have an email")
        if not username:
            raise ValueError("Users must have an username")
        
        user = self.model(
            email = self.normalize_email(email),
            username = username,
            fullname = fullname,
            password = make_password(password)
        )
        user.save(using=self._db)
        return user
    def create_superuser(self, username, fullname, email, password):
        if not email:
            raise ValueError("Users must have an email")
        if not username:
            raise ValueError("Users must have an username")
        
        user = self.model(
            email = self.normalize_email(email),
            username = username,
            fullname = fullname,
            password = make_password(password),
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
class Account(AbstractBaseUser):
    fullname = models.CharField(verbose_name="fullname", max_length=500)
    email = models.EmailField(verbose_name="email", max_length=250, unique=True)
    username = models.CharField(verbose_name="username", max_length=250, unique=True)
    date_joined = models.DateTimeField(verbose_name="date_joined", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="last_login", auto_now=True)
    is_admin = models.BooleanField(verbose_name="is_admin", default=False)
    is_superuser = models.BooleanField(verbose_name="is_superuser", default=False)
    is_staff = models.BooleanField(verbose_name="is_staff", default=False)
    is_active = models.BooleanField(verbose_name="is_active", default=True)
    hide_email = models.BooleanField(verbose_name="hide_email", default=True)

    REQUIRED_FIELDS = ['email', 'fullname']
    USERNAME_FIELD = 'username'

    objects = AccountManager()

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True
    
    def has_module_perms(self, obj=None):
        return True