# Generated by Django 3.0.8 on 2020-07-28 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0038_auto_20200728_0610'),
    ]

    operations = [
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Profile_Name', models.CharField(max_length=100, unique=True)),
                ('borrower_status', models.CharField(default=False, max_length=100)),
                ('gender', models.CharField(default=None, max_length=100)),
                ('age', models.CharField(default=None, max_length=100)),
                ('current_residence', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('education', models.CharField(default=None, max_length=100)),
                ('car', models.CharField(default=None, max_length=100)),
                ('household_income', models.CharField(max_length=100)),
                ('daily_internet_usage', models.CharField(default=None, max_length=100)),
                ('Pet', models.CharField(default=None, max_length=100)),
                ('employment_status', models.CharField(default=None, max_length=100)),
                ('employment_industry', models.CharField(default=None, max_length=100)),
                ('exercise', models.CharField(default=None, max_length=100)),
                ('social_media', models.CharField(default=None, max_length=100)),
                ('Purchases', models.CharField(default=None, max_length=100)),
                ('news_sources', models.CharField(default=None, max_length=100)),
                ('travel_frequency', models.CharField(default=None, max_length=100)),
                ('marital_status', models.CharField(default=None, max_length=100)),
                ('political_affiliation', models.CharField(default=None, max_length=100)),
                ('Kids', models.CharField(blank=True, default=False, max_length=100, null=True)),
                ('Smoker', models.CharField(default=None, max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Surveys',
        ),
    ]