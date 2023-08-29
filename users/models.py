from django.contrib.auth.models import AbstractUser
from django.db import models

from catalog.models import NULLABLE


class User(AbstractUser):
    """Модель для пользователя"""

    username = None
    email = models.EmailField(unique=True, verbose_name='почта')

    email_is_confirmed = models.BooleanField(default=False, verbose_name='подтверждено')
    email_confirm_key = models.CharField(max_length=30, verbose_name='код подтверждения почты', **NULLABLE)

    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', **NULLABLE)
    phone = models.CharField(max_length=35, verbose_name='телефон', **NULLABLE)
    country = models.CharField(**NULLABLE, verbose_name='страна')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
