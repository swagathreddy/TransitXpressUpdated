# Generated by Django 4.2.7 on 2024-01-25 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transitXpress', '0010_feature_arrival_time_feature_bus_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='feature',
            name='place_notes',
            field=models.TextField(blank=True, default='Intersting place to visit', null=True),
        ),
    ]
