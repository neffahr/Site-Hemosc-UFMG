# Generated by Django 4.2.1 on 2023-07-11 19:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bolsas', '0007_alter_bloodbag_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bloodbag',
            name='location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='bolsas.hemocentro'),
        ),
    ]
