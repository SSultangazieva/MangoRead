from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, AbstractUser, UserManager
from django.db import models


class User_name(AbstractBaseUser):
    username = models.CharField("Имя", max_length=100, blank=True, null=True, unique=True)
    email = models.EmailField("Почта", unique=True, null=True)
    password = models.CharField("введите почту", max_length=40, unique=True)
    objects = UserManager()
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=True)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['password', 'email']

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

