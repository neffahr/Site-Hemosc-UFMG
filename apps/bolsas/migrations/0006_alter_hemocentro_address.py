# Generated by Django 4.2.1 on 2023-07-09 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bolsas', '0005_alter_hemocentro_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hemocentro',
            name='address',
            field=models.CharField(choices=[('FLORIANÓPOLIS', 'Florianópolis'), ('JOINVILLE', 'Joinville'), ('BLUMENAU', 'Blumenau'), ('CRICIÚMA', 'Criciúma'), ('LAGES', 'Lages'), ('JOAÇABA', 'Joaçaba'), ('CHAPECÓ', 'Chapecó')], max_length=20),
        ),
    ]
