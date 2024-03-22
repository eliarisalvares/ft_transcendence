# Generated by Django 5.0.1 on 2024-03-22 01:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_enable_2fa_in_user_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='BaseSignUpDto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('user_name', models.CharField(max_length=100)),
            ],
            options={
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SignInDto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=100)),
            ],
            options={
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SignInUpOAuth42Dto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('acess_token', models.CharField(max_length=100)),
                ('expires_in', models.IntegerField()),
                ('user_name', models.CharField(max_length=100)),
            ],
            options={
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UserEditDto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('enable_2fa', models.BooleanField()),
                ('password', models.CharField(max_length=100)),
                ('old_password', models.CharField(max_length=100)),
            ],
            options={
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SignUpDto',
            fields=[
                ('basesignupdto_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='app.basesignupdto')),
                ('password', models.CharField(max_length=100)),
            ],
            options={
                'managed': False,
            },
            bases=('app.basesignupdto',),
        ),
    ]
