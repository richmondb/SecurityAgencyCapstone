# Generated by Django 4.0.5 on 2022-08-06 00:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('security', '0003_delete_duration'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contract',
            name='nbi',
        ),
    ]
