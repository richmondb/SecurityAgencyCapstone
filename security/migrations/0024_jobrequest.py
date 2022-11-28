# Generated by Django 4.0.5 on 2022-08-08 07:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import security.models


class Migration(migrations.Migration):

    dependencies = [
        ('security', '0023_alter_customuser_position'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issued_date', models.DateField(default=security.models.start_time)),
                ('start_date', models.DateField(null=True)),
                ('years', models.IntegerField(null=True)),
                ('months', models.IntegerField(null=True)),
                ('daily_wage', models.FloatField(null=True)),
                ('for_approval', models.BooleanField(default=False)),
                ('is_finished', models.BooleanField(default=False)),
                ('link', models.URLField(blank=True, max_length=150, null=True)),
                ('client', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='job_requests', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
