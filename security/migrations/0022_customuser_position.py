# Generated by Django 4.0.5 on 2022-08-08 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('security', '0021_customuser_sex'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='position',
            field=models.CharField(default='Principal', max_length=150, null=True),
        ),
    ]
