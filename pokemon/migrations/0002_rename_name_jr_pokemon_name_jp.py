# Generated by Django 4.0.4 on 2022-10-11 17:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pokemon',
            old_name='name_jr',
            new_name='name_jp',
        ),
    ]
