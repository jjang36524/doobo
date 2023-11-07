# Generated by Django 4.2.7 on 2023-11-06 23:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dooboard', '0004_rename_save_pitcherdata_saves'),
    ]

    operations = [
        migrations.CreateModel(
            name='PitcherDataLS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ERA', models.FloatField()),
                ('K', models.IntegerField()),
                ('inning', models.FloatField()),
                ('win', models.IntegerField()),
                ('loss', models.IntegerField()),
                ('saves', models.IntegerField()),
                ('hold', models.IntegerField()),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dooboard.player')),
            ],
        ),
        migrations.CreateModel(
            name='BatterDataLS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('AVG', models.FloatField()),
                ('OBP', models.FloatField()),
                ('SLG', models.FloatField()),
                ('PA', models.IntegerField()),
                ('hit', models.IntegerField()),
                ('homerun', models.IntegerField()),
                ('BOB', models.IntegerField()),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dooboard.player')),
            ],
        ),
    ]
