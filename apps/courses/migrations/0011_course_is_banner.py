# Generated by Django 2.1.7 on 2019-03-05 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0010_merge_20190304_2117'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='is_banner',
            field=models.BooleanField(default=False, verbose_name='是否轮播'),
        ),
    ]
