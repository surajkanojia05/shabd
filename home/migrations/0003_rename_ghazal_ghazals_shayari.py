# Generated by Django 3.2.5 on 2021-07-07 08:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_rename_singer_ghazals_writer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ghazals',
            old_name='ghazal',
            new_name='shayari',
        ),
    ]
