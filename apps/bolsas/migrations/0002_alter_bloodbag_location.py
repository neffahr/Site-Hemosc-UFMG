# Generated by Django 4.2.1 on 2023-07-14 17:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bolsas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bloodbag',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='bolsas.hemocentro'),
        ),
    ]