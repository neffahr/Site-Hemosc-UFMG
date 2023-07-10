# Generated by Django 4.2.1 on 2023-06-28 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bolsas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bloodbag',
            name='level',
            field=models.CharField(choices=[('CRITICO', 'Crítico'), ('BAIXO', 'Baixo'), ('ESTAVEL', 'Estável'), ('ADEQUADO', 'Adequado')], max_length=10),
        ),
        migrations.AlterField(
            model_name='bloodbag',
            name='type',
            field=models.CharField(choices=[('A+', 'A+'), ('B+', 'B+'), ('AB+', 'AB+'), ('O+', 'O+'), ('A-', 'A-'), ('B-', 'B-'), ('AB-', 'AB-'), ('O-', 'O-')], max_length=3),
        ),
    ]