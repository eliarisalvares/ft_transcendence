# Generated by Django 5.0.3 on 2024-05-07 02:46
import uuid
from django.db import migrations, models


def forwards(apps, schema_editor):
    user = apps.get_model("user", "User")

    users_list = user.objects.all()
    for u in users_list:
        if not u.username:
            u.username = f"username_{str(uuid.uuid4())[:10]}"
            u.save()

def backwards(apps, schema_editor):
    # table will be deleted in next operation
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_user_username'),
    ]

    operations = [
        migrations.RunPython(forwards, backwards),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]