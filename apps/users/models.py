from django.db import models
from django.contrib.auth.models import AbstractUser

class HemoscUser(AbstractUser):
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