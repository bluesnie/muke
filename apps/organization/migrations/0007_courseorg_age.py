# Generated by Django 2.1.7 on 2019-03-04 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0006_auto_20190301_0959'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseorg',
            name='age',
            field=models.IntegerField(default=18, verbose_name='年龄'),
        ),
    ]
