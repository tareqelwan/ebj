# Generated by Django 4.0.1 on 2022-01-14 16:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('setup', '0001_initial'),
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='salesman',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='setup.salesman'),
        ),
    ]
