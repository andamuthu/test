# Generated by Django 3.0.8 on 2020-07-26 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0008_remove_survey_kids'),
    ]

    operations = [
        migrations.AddField(
            model_name='survey',
            name='Kids',
            field=models.CharField(blank=True, choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7+', '7+')], default=None, max_length=100, null=True),
        ),
    ]
