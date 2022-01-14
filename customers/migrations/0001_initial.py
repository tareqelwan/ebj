# Generated by Django 4.0.1 on 2022-01-14 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('name_arb', models.CharField(max_length=100)),
                ('buildno', models.CharField(max_length=10)),
                ('street', models.CharField(max_length=50)),
                ('district', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=10)),
                ('country', models.CharField(max_length=10)),
                ('postalcode', models.CharField(max_length=10)),
                ('additionalno', models.CharField(max_length=10)),
                ('buildno_a', models.CharField(max_length=10)),
                ('street_a', models.CharField(max_length=50)),
                ('district_a', models.CharField(max_length=50)),
                ('city_a', models.CharField(max_length=10)),
                ('country_a', models.CharField(max_length=10)),
                ('postalcode_a', models.CharField(max_length=10)),
                ('additionalno_a', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=30)),
                ('phone', models.CharField(max_length=30)),
                ('vat_id', models.CharField(max_length=30)),
                ('crlimit', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('crdays', models.IntegerField(default=0)),
                ('ctype', models.CharField(choices=[('1', 'Company'), ('2', 'Person'), ('3', 'Government'), ('4', 'Others'), ('5', 'Super dealer'), ('6', 'Contractor'), ('7', 'Owner'), ('8', 'Hyper'), ('9', 'Power retailer')], max_length=1)),
                ('cgroup', models.CharField(choices=[('1', 'Customer'), ('2', 'Supplier')], max_length=1)),
            ],
        ),
    ]