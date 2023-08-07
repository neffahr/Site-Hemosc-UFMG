from django.db import models
from datetime import datetime

class Hemocentro(models.Model):
    choices=[
            ("FLORIANÓPOLIS", "Florianópolis"),
            ("JOINVILLE", "Joinville"),
            ("BLUMENAU", "Blumenau"),
            ("CRICIÚMA", "Criciúma"),
            ("LAGES", "Lages"),
            ("JOAÇABA", "Joaçaba"),
            ("CHAPECÓ", "Chapecó")
    ]
    address = models.CharField(max_length=20, choices=choices)
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
    location = models.ForeignKey(Hemocentro, on_delete=models.PROTECT)

    def calc_ideal_qnt(self, new_data):
        data = self.dataarray_set.all()

        min = None
        for i in data:
            min = i.id if min == None or min > i.id else min
        DataArray.objects.create(total=new_data, bag=self)
        DataArray.objects.get(pk=min).delete()

        ideal_qnt = 0
        data = self.dataarray_set.all()
        for item in data:
            ideal_qnt += item.total
        return ideal_qnt//7
    
    def calc_level(self):
        total_bags = self.total
        if (total_bags <= (self.ideal_qnt//4)):
            return 'CRITICO'
        elif (total_bags <= (3*self.ideal_qnt//5)):
            return 'BAIXO'
        elif (total_bags < (self.ideal_qnt)):
            return 'ESTAVEL'
        else:
            return 'ADEQUADO'

    def __str__(self):
        return self.type

class DataArray(models.Model):
    total = models.IntegerField()
    bag = models.ForeignKey(BloodBag, on_delete=models.PROTECT)

    def __str__(self):
        return str(self.total)


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
        return qnt/7
    
    def calc_total(self, type):
        qnt = 0
        for bag in BloodBag.objects.filter(type=type):
            qnt += bag.total
        return qnt/7 
    
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
