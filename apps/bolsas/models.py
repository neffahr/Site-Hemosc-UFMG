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

class IndexBag:
    def __init__(self, type):
        self.type = type
        self.total = self.calc_total(type)
        self.ideal_qnt = self.calc_ideal_qnt(type)
        self.level = self.calc_level(type)
    
    def calc_ideal_qnt(self, type):
        qnt = 0
        for bag in BloodBag.objects.filter(type=type):
            qnt += bag.ideal_qnt
        return qnt/2
    
    def calc_total(self, type):
        qnt = 0
        for bag in BloodBag.objects.filter(type=type):
            qnt += bag.total
        return qnt/2
    
    def calc_level(self, type):
        total_bags = self.calc_total(type)
        if (total_bags <= (self.ideal_qnt//4)):
            return 'Crítico'
        elif (total_bags <= (3*self.ideal_qnt//5)):
            return 'Baixo'
        elif (total_bags < (self.ideal_qnt)):
            return 'Estável'
        else:
            return 'Adequado'
