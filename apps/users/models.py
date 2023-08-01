from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager

class HemoscUser(AbstractUser):
    email = models.EmailField(unique=True)
    location = models.CharField(
        max_length=20, 
        choices=[
            ("FLORIANÓPOLIS", "Florianópolis"),
            ("JOINVILLE", "Joinville"),
            ("BLUMENAU", "Blumenau"),
            ("CRICIÚMA", "Criciúma"),
            ("LAGES", "Lages"),
            ("JOAÇABA", "Joaçaba"),
            ("CHAPECÓ", "Chapecó")
        ],
    )
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


class HemoscUserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Users require an email field')
        if not password:
            raise ValueError('Users require a password field')
        
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_user(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(email, password, **extra_fields)