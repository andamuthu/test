# Generated by Django 3.0.8 on 2020-07-27 15:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0030_auto_20200727_1558'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='survey',
            name='Kids',
        ),
    ]