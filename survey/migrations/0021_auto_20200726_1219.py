# Generated by Django 3.0.8 on 2020-07-26 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0020_auto_20200726_1217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='survey',
            name='Kids',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7+', '7+')], default=None, max_length=100),
        ),
    ]
