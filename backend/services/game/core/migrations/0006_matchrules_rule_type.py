# Generated by Django 5.0.3 on 2024-04-22 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_remove_matchrules_all_rules_null_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='matchrules',
            name='rule_type',
            field=models.CharField(choices=[(0, 'Player winner points'), (1, 'Match total points'), (2, 'Match duartion'), (3, 'Mixed rules')], default=0, max_length=1, verbose_name='Match rule type'),
        ),
    ]