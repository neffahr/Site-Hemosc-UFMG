# Generated by Django 4.2.1 on 2023-07-09 15:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bolsas', '0003_rename_quantity_bloodbag_total'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hemocentro',
            name='ideal_qnt',
        ),
    ]
