# Generated by Django 4.0.5 on 2022-08-07 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('security', '0011_alter_contract_issued_date'),
    ]

    operations = [
        migrations.DeleteModel(
            name='License',
        ),
        migrations.AddField(
            model_name='guard',
            name='lesp_issued_date',
            field=models.DateField(null=True),
        ),
        migrations.DeleteModel(
            name='NBI',
        ),
    ]
