# Generated by Django 4.0.4 on 2022-04-13 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_account_prc_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='prc_pic',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
