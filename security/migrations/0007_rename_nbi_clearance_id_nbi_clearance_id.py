# Generated by Django 4.0.5 on 2022-08-06 00:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('security', '0006_nbi'),
    ]

    operations = [
        migrations.RenameField(
            model_name='nbi',
            old_name='nbi_clearance_id',
            new_name='clearance_id',
        ),
    ]
