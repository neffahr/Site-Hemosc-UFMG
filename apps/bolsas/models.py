from django.db import models
from datetime import datetime

class Hemocentro(models.Model):
    address = models.CharField(max_length=20)
    last_updated = models.DateTimeField(default=datetime.now, blank=False)

    def __str__(self):
        return self.address


class BloodBag(models.Model):
    TYPES = [
        ('A+', 'A+'), ('B+', 'B+'), ('AB+', 'AB+'), ('O+', 'O+'),
        ('A-', 'A-'), ('B-', 'B-'), ('AB-', 'AB-'), ('O-', 'O-')
    ]
    LEVELS = [
        ('CRITICO', 'Crítico'), ('BAIXO', 'Baixo'), ('ESTAVEL', 'Estável'), ('ADEQUADO', 'Adequado')
    ]

    type = models.CharField(max_length=3, choices=TYPES)
    level = models.CharField(max_length=10, choices=LEVELS)
    ideal_qnt = models.IntegerField()
    total = models.IntegerField()
    last_updated = models.DateTimeField(default=datetime.now)
    location = models.ForeignKey(Hemocentro, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.type

