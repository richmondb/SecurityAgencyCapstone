# Generated by Django 4.0.5 on 2022-08-08 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('security', '0020_delete_jobrequest'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='sex',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='M', max_length=1),
        ),
    ]
