from django.db import models
from django.contrib.auth.models import AbstractUser

class HemoscUser(AbstractUser):
    location = models.CharField(
        max_length=20, 
        choices=[
            ("FLORIANOPOLIS", "Florianópolis"),
            ("JOINVILLE", "Joinville"),
            ("BLUMENAU", "Blumenau"),
            ("CRICIUMA", "Criciúma"),
            ("LAGES", "Lages"),
            ("JOACABA", "Joaçaba"),
            ("CHAPECO", "Chapecó")
        ],
    )