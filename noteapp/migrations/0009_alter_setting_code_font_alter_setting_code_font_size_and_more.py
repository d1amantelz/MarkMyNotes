# Generated by Django 5.0.4 on 2024-05-14 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noteapp', '0008_alter_setting_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='setting',
            name='code_font',
            field=models.CharField(choices=[('JetBrains Mono', 'JetBrains Mono'), ('Nunito', 'Nunito'), ('Fira Code', 'Fira Code'), ('Roboto Thin', 'Roboto Thin'), ('Source Code Pro', 'Source Code Pro')], default='JetBrains Mono', max_length=20),
        ),
        migrations.AlterField(
            model_name='setting',
            name='code_font_size',
            field=models.IntegerField(choices=[(12, '12'), (14, '14'), (16, '16'), (18, '18')], default=14),
        ),
        migrations.AlterField(
            model_name='setting',
            name='text_font',
            field=models.CharField(choices=[('JetBrains Mono', 'JetBrains Mono'), ('Nunito', 'Nunito'), ('Fira Code', 'Fira Code'), ('Roboto Thin', 'Roboto Thin'), ('Source Code Pro', 'Source Code Pro')], default='JetBrains Mono', max_length=20),
        ),
        migrations.AlterField(
            model_name='setting',
            name='text_font_size',
            field=models.IntegerField(choices=[(12, '12'), (14, '14'), (16, '16'), (18, '18')], default=16),
        ),
    ]
