# Generated by Django 4.2.7 on 2023-11-13 04:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dooboard', '0013_alter_player_voterd_alter_player_voteru_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='author',
        ),
    ]
