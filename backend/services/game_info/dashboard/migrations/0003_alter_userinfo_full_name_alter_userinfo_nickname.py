# Generated by Django 5.0.1 on 2024-05-22 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_alter_userinfo_losses_alter_userinfo_position_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='full_name',
            field=models.CharField(max_length=50, verbose_name='full_name'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='nickname',
            field=models.CharField(max_length=10, verbose_name='nickname'),
        ),
    ]
