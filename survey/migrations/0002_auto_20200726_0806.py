# Generated by Django 3.0.8 on 2020-07-26 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='survey',
            name='gender',
            field=models.CharField(choices=[('---', ''), ('Male', 'Male'), ('Female', 'Female'), ('N/A', 'N/A')], default=False, max_length=100),
        ),
    ]