# Generated by Django 3.0.8 on 2020-07-27 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0025_auto_20200727_1519'),
    ]

    operations = [
        migrations.AlterField(
            model_name='survey',
            name='borrower_status',
            field=models.CharField(default=False, max_length=100),
        ),
    ]
