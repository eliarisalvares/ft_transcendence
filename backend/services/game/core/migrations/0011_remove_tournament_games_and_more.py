# Generated by Django 5.0.3 on 2024-05-04 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_alter_tournament_tournament_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tournament',
            name='games',
        ),
        migrations.RemoveField(
            model_name='tournament',
            name='number_of_games',
        ),
        migrations.AddField(
            model_name='tournament',
            name='number_of_rounds',
            field=models.PositiveSmallIntegerField(default=1),
        ),
        migrations.CreateModel(
            name='Round',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_of_games', models.PositiveSmallIntegerField(default=0)),
                ('round_number', models.IntegerField(default=1)),
                ('games', models.ManyToManyField(related_name='round', to='core.game', verbose_name='Games')),
            ],
        ),
        migrations.AddField(
            model_name='tournament',
            name='rounds',
            field=models.ManyToManyField(related_name='tournament', to='core.round', verbose_name='Rounds'),
        ),
    ]