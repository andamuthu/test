# Generated by Django 3.0.8 on 2020-07-26 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0004_survey_borrower_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='survey',
            name='Borrower_Status',
        ),
        migrations.AddField(
            model_name='survey',
            name='Kids',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7+', '7+')], default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='survey',
            name='Pet',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='survey',
            name='Purchases',
            field=models.CharField(choices=[('Automotive Parts', 'Automotive Parts'), ('Baby & Kids', 'Baby & Kids'), ('Books', 'Books'), ('Clothing & Shoes', 'Clothing & Shoes'), ('Electronics and Computers', 'Electronics and Computers'), ('Groceries & Food', 'Groceries & Food'), ('Handmade Products', 'Handmade Products'), ('Health & Beauty', 'Health & Beauty'), ('Home & Garden', 'Home & Garden'), ('Jewelry', 'Jewelry'), ('Movies', 'Movies'), ('Music', 'Music'), ('Sports & Outdoors', 'Sports & Outdoors'), ('Toys', 'Toys'), ('Videogames', 'Videogames')], default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='survey',
            name='Smoker',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='survey',
            name='borrower_status',
            field=models.CharField(choices=[('Auto Loan', 'Auto Loan'), ('Business Loan', 'Business Loan'), ('Credit Cards', 'Credit Cards'), ('Home Mortgage', 'Home Mortgage'), ('Student Loan', 'Student Loan'), ('Personal Loan', 'Personal Loan')], default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='survey',
            name='current_residence',
            field=models.CharField(choices=[('Own', 'Own'), ('Rent', 'Rent')], default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='survey',
            name='daily_internet_usage',
            field=models.CharField(choices=[('1 to 4 hours', '1 to 4 hours'), ('5 to 7 hours', '5 to 7 hours'), ('7 + hours', '7 + hours')], default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='survey',
            name='education',
            field=models.CharField(choices=[('High school', 'High school'), ('Bachelors degree', 'Bachelors degree'), ('Graduate degree', 'Graduate degree')], default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='survey',
            name='employment_industry',
            field=models.CharField(choices=[('Banking & Financial Services', 'Banking & Financial Services'), ('Education', 'Education'), ('Food and Beverage', 'Food and Beverage'), ('Government & Non-Profit', 'Government & Non-Profit'), ('Healthcare', 'Healthcare'), ('Manufacturing', 'Manufacturing'), ('Media & Entertainment', 'Media & Entertainment'), ('Retail, Wholesale & Distribution', 'Retail, Wholesale & Distribution'), ('Software & IT Services', 'Software & IT Services')], default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='survey',
            name='employment_status',
            field=models.CharField(choices=[('Full Time (35+ hours per week)', 'Full Time (35+ hours per week)'), ('Part Time (1-34 hours per week)', 'Part Time (1-34 hours per week)')], default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='survey',
            name='exercise',
            field=models.CharField(choices=[('Every Day', 'Every Day'), ('4+ Times/Week', '4+ Times/Week'), ('2-3 Times/Week', '2-3 Times/Week'), ('Once/Week', 'Once/Week'), ('Not at All', 'Not at All')], default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='survey',
            name='household_income',
            field=models.CharField(choices=[('$0 - $24,999', '$0 - $24,999'), ('$25,000 - $49,999', '$25,000 - $49,999'), ('$50,000 - $74,999', '$50,000 - $74,999'), ('$75,000 - $99,999', '$75,000 - $99,999'), ('$100,000 - $149,999', '$100,000 - $149,999'), ('$150, 000 or more', '$150, 000 or more')], default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='survey',
            name='marital_status',
            field=models.CharField(choices=[('Single', 'Single'), ('Married', 'Married'), ('Divorced', 'Divorced')], default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='survey',
            name='news_sources',
            field=models.CharField(choices=[('Podcasts', 'Podcasts'), ('Print', 'Print'), ('Radio', 'Radio'), ('Social Media', 'Social Media'), ('TV (Late Night Comedy, Other)', 'TV (Late Night Comedy, Other)'), ('TV (Local/Cable News)', 'TV (Local/Cable News)'), ('Word of Mouth', 'Word of Mouth')], default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='survey',
            name='own',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='survey',
            name='political_affiliation',
            field=models.CharField(choices=[('Conservative', 'Conservative'), ('Liberal', 'Liberal'), ('Moderate', 'Moderate')], default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='survey',
            name='social_media',
            field=models.CharField(choices=[('Facebook', 'Facebook'), ('Google', 'Google'), ('Twitter', 'Twitter'), ('Instagram', 'Instagram'), ('LinkedIn', 'LinkedIn'), ('Youtube', 'Youtube'), ('Pinterest', 'Pinterest'), ('Reddit', 'Reddit'), ('Tumblr', 'Tumblr')], default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='survey',
            name='travel_frequency',
            field=models.CharField(choices=[('Never', 'Never'), ('Every Few Years', 'Every Few Years'), ('Every Year', 'Every Year'), ('Every Quarter', 'Every Quarter'), ('Every Month', 'Every Month')], default=None, max_length=100),
        ),
    ]
