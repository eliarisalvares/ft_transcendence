# Generated by Django 3.2.25 on 2024-05-07 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_management_api', '0005_rename_user_id_user_user_uuid'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='avatar_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
