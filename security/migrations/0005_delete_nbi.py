# Generated by Django 4.0.5 on 2022-08-06 00:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('security', '0004_remove_contract_nbi'),
    ]

    operations = [
        migrations.DeleteModel(
            name='NBI',
        ),
    ]
