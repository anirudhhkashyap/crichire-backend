# Generated by Django 3.1.4 on 2021-01-06 15:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0003_fixture_player_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fixture',
            old_name='player_id',
            new_name='player',
        ),
    ]
