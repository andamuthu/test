# Generated by Django 3.0.8 on 2020-07-28 07:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0045_remove_survey_current_residence'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='survey',
            name='Profile_Name',
        ),
        migrations.RemoveField(
            model_name='survey',
            name='age',
        ),
        migrations.RemoveField(
            model_name='survey',
            name='borrower_status',
        ),
        migrations.RemoveField(
            model_name='survey',
            name='gender',
        ),
    ]
