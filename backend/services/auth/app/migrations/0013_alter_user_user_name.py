# Generated by Django 5.0.1 on 2024-05-26 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app','0012_alter_twofactor_expiration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
