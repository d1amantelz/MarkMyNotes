# Generated by Django 5.0.4 on 2024-05-27 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noteapp', '0002_alter_note_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='is_pinned',
            field=models.BooleanField(default=False),
        ),
    ]