# Generated by Django 3.0.8 on 2020-07-27 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0035_auto_20200727_1649'),
    ]

    operations = [
        migrations.AlterField(
            model_name='survey',
            name='current_residence',
            field=models.CharField(default=None, max_length=100),
        ),
    ]