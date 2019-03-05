# Generated by Django 2.0.6 on 2019-03-05 17:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gameApp', '0003_auto_20190305_1620'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gamemodel',
            name='game_model',
        ),
        migrations.AddField(
            model_name='gamemodel',
            name='gamer_key',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='gameApp.UserModel'),
        ),
    ]
