# Generated by Django 4.2.7 on 2024-01-25 18:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transitXpress', '0021_alter_feature_place_notes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='confirmation',
            name='unique_code',
        ),
    ]
