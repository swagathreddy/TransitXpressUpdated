# Generated by Django 4.2.7 on 2024-01-25 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transitXpress', '0020_remove_confirmation_nique_code_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feature',
            name='place_notes',
            field=models.TextField(blank=True, default='Interesting place to visit', null=True),
        ),
    ]
