# Generated by Django 3.0.8 on 2020-07-26 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0010_auto_20200726_1156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='survey',
            name='Kids',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], default=None, max_length=100, null=True),
        ),
    ]
