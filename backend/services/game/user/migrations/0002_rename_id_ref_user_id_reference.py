# Generated by Django 5.0.3 on 2024-04-21 04:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='id_ref',
            new_name='id_reference',
        ),
    ]
