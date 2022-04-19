# Generated by Django 4.0.4 on 2022-04-19 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_alter_account_provider_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='password',
            field=models.CharField(default='none', max_length=100),
        ),
        migrations.AlterField(
            model_name='account',
            name='provider_type',
            field=models.CharField(choices=[('N/A', 'Not Applicable'), ('Doctor', 'Doctor'), ('Pharmacist', 'Pharmacist')], default='N/A', max_length=20),
        ),
    ]
