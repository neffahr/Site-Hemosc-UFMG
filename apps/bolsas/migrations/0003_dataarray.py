# Generated by Django 4.2.1 on 2023-08-01 01:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bolsas', '0002_alter_bloodbag_location'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataArray',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.IntegerField()),
                ('bag', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='bolsas.bloodbag')),
            ],
        ),
    ]
