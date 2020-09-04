from django.contrib.postgres.fields import ArrayField
from django.db import models


class Survey(models.Model):
    borrower_status = models.CharField(max_length=100, default=False)
    Profile_Name = models.CharField(max_length=100, unique=True)
    gender = models.CharField(max_length=100, default=False)
    age = models.CharField(max_length=100, default=False, choices=AGE_CHOICES)
    current_residence = models.CharField(max_length=100, default=None, choices=RESIDENCE)
    education = models.CharField(max_length=100, default=None, choices=EDUCATION)
    own = models.CharField(max_length=100, default=None, choices=OWN)
    household_income = models.CharField(max_length=100, default=None, choices=HOUSEHOLD_INCOME)
    daily_internet_usage = models.CharField(max_length=100, default=None, choices=DAILY_INTERNET_USAGE)
    Pet = models.CharField(max_length=100, default=None, choices=PET)
    employment_status = models.CharField(max_length=100, default=None, choices=EMPLOYMENT_STATUS)
    employment_industry = models.CharField(max_length=100, default=None, choices=EMPLOYMENT_INDUSTRY)
    exercise = models.CharField(max_length=100, default=None, choices=EXERCISE)
    social_media = models.CharField(max_length=100, default=None, choices=SOCIAL_MEDIA)
    Purchases = models.CharField(max_length=100, default=None, choices=PURCHASES)
    news_sources = models.CharField(max_length=100, default=None, choices=NEWS_SOURCES)
    travel_frequency = models.CharField(max_length=100, default=None, choices=TRAVEL_FREQUENCY)
    marital_status = models.CharField(max_length=100, default=None, choices=MARITAL_STATUS)
    political_affiliation = models.CharField(max_length=100, default=None, choices=POLITICAL_AFFILIATION)
    Kids = models.CharField(max_length=100, default=None, choices=KIDS)
    Smoker = models.CharField(max_length=100, default=None, choices=SMOKER)

    def __unicode__(self):
        return self.Profile_Name
