# Generated by Django 3.2.25 on 2024-05-18 20:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_management_api', '0008_alter_friendshiprequest_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='blockeduser',
            unique_together=set(),
        ),
        migrations.AlterUniqueTogether(
            name='friendship',
            unique_together=set(),
        ),
    ]
