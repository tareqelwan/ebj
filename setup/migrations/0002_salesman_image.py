# Generated by Django 4.0.1 on 2022-01-14 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('setup', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='salesman',
            name='image',
            field=models.ImageField(default='', upload_to='sman/'),
            preserve_default=False,
        ),
    ]
