# Generated by Django 2.1.7 on 2019-03-04 15:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20190223_1245'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='birday',
            new_name='birthday',
        ),
    ]
