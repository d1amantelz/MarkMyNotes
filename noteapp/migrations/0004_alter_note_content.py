# Generated by Django 5.0.4 on 2024-05-31 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noteapp', '0003_note_is_pinned'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='content',
            field=models.TextField(blank=True, default=''),
        ),
    ]
