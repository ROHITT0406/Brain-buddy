# Generated by Django 5.1.3 on 2024-11-24 17:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_user_avater'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='avater',
            new_name='avatar',
        ),
    ]
