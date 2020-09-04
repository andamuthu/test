from django.db import models


class Survey(models.Model):
    Profile_Name = models.CharField(max_length=100, unique=True)
    gender = models.CharField(max_length=100, default=None)
    age = models.CharField(max_length=100, default=None)
    borrower_status = models.CharField(max_length=100, default=False)
    current_residence = models.CharField(max_length=100, default=None, null=True, blank=True)
    education = models.CharField(max_length=100, default=None, null=True, blank=True)
    car = models.CharField(max_length=100, default=None)
    household_income = models.CharField(max_length=100)
    daily_internet_usage = models.CharField(max_length=100, default=None)
    Pet = models.CharField(max_length=100, default=None)
    employment_status = models.CharField(max_length=100, default=None)
    employment_industry = models.CharField(max_length=100, default=None)
    exercise = models.CharField(max_length=100, default=None)
    social_media = models.CharField(max_length=100, default=None)
    Purchases = models.CharField(max_length=100, default=None)
    news_sources = models.CharField(max_length=100, default=None)
    travel_frequency = models.CharField(max_length=100, default=None)
    marital_status = models.CharField(max_length=100, default=None)
    political_affiliation = models.CharField(max_length=100, default=None)
    Kids = models.CharField(max_length=100, default=False, null=True,blank=True)
    Smoker = models.CharField(max_length=100, default=None)

    def __unicode__(self):
        return self.Profile_Name
