# Generated by Django 4.2.7 on 2023-11-06 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dooboard', '0002_rename_whip_pitcherdata_era_alter_batterdata_obp_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='image',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
