from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, identification, phone_number='', chat_name='', password=None, name=None):
        user = self.model(
            identification=identification,
            phone_number=phone_number,
            chat_name=chat_name,
            name=name
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, identification, phone_number='', password=None):
        user = self.create_user(
            identification=identification,
            phone_number=phone_number,
            password=password
        )
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    objects = UserManager()

    identification = models.CharField(max_length=30, null=False, unique=True)
    name = models.CharField(max_length=10, null=True)
    phone_number = models.CharField(max_length=11, null=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    fcm_token = models.CharField(max_length=300, null=True)

    chat_name = models.CharField(max_length=20, null=True, default='동대표')

    USERNAME_FIELD = 'identification'
    REQUIRED_FIELDS = ['phone_number']

    def __str__(self):
        return '{}. {}'.format(self.id, self.identification)
