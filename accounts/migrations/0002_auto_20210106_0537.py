# Generated by Django 3.1.4 on 2021-01-06 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('player', 'Player'), ('manager', 'Manager')], max_length=7),
        ),
    ]
