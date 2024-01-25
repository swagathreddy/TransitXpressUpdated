# Generated by Django 4.2.7 on 2024-01-25 11:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('transitXpress', '0011_feature_place_notes'),
    ]

    operations = [
        migrations.AddField(
            model_name='confirmation',
            name='booking_date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
