# Generated by Django 3.1.4 on 2021-01-06 15:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0002_auto_20210106_0428'),
    ]

    operations = [
        migrations.AddField(
            model_name='fixture',
            name='player_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='players.player'),
        ),
    ]
