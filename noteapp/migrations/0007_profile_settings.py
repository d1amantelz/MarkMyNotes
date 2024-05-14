# Generated by Django 5.0.4 on 2024-05-14 09:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noteapp', '0006_alter_setting_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='settings',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='noteapp.setting'),
        ),
    ]