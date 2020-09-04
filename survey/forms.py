from django import forms
from survey.choices import *
from survey.models import *


class SurveyForm(forms.ModelForm):
    borrower_status = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple(), choices=BORROWER_STATUS,
                                                label="Borrower Status. Check All That Apply.")
    gender = forms.ChoiceField(choices=GENDER_CHOICES)
    current_residence = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple(), choices=RESIDENCE)
    age = forms.ChoiceField(widget=forms.RadioSelect(), choices=AGE_CHOICES)
    education = forms.ChoiceField(widget=forms.RadioSelect(), choices=EDUCATION)
    car = forms.ChoiceField(widget=forms.RadioSelect(), choices=CAR, label="Do You Own a Car?")
    household_income = forms.ChoiceField(widget=forms.RadioSelect(), choices=HOUSEHOLD_INCOME)
    daily_internet_usage = forms.ChoiceField(widget=forms.RadioSelect(),
                                             choices=DAILY_INTERNET_USAGE)
    Pet = forms.ChoiceField(widget=forms.RadioSelect(), choices=PET, label="Do You Own a Pet?")
    employment_status = forms.ChoiceField(widget=forms.RadioSelect(), choices=EMPLOYMENT_STATUS)
    employment_industry = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple(), choices=EMPLOYMENT_INDUSTRY)
    exercise = forms.ChoiceField(widget=forms.RadioSelect(), choices=EXERCISE)
    social_media = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple(), choices=SOCIAL_MEDIA,
                                             label="Social Media/ Tech Platform User? Check All That Apply.")
    Purchases = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple(), choices=PURCHASES,
                                          label="Online Purchases. Check all that apply.")
    news_sources = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple(), choices=NEWS_SOURCES,
                                             label="Primary News Sources. Check all that apply.")
    travel_frequency = forms.ChoiceField(widget=forms.RadioSelect(), choices=TRAVEL_FREQUENCY,
                                         label="Vacation/Travel Frequency")
    marital_status = forms.ChoiceField(widget=forms.RadioSelect(), choices=MARITAL_STATUS)
    political_affiliation = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple(),
                                                      choices=POLITICAL_AFFILIATION)
    Kids = forms.ChoiceField(choices=KIDS, label="How Many Kids Do You Have?")
    Smoker = forms.ChoiceField(widget=forms.RadioSelect(), choices=SMOKER)

    class Meta:
        model = Survey
        fields = '__all__'
        # widgets = {'age': forms.RadioSelect(),
        #            'borrower_status': forms.CheckboxSelectMultiple,
        #            'current_residence': forms.CheckboxSelectMultiple,
        #            'education': forms.RadioSelect(),
        #            'own': forms.RadioSelect(),
        #            'household_income': forms.RadioSelect(),
        #            'daily_internet_usage': forms.RadioSelect(),
        #            'Pet': forms.RadioSelect(),
        #            'employment_status': forms.RadioSelect(),
        #            'employment_industry': forms.CheckboxSelectMultiple,
        #            'exercise': forms.RadioSelect(),
        #            'social_media': forms.CheckboxSelectMultiple,
        #            'Purchases': forms.CheckboxSelectMultiple,
        #            'news_sources': forms.CheckboxSelectMultiple,
        #            'travel_frequency': forms.RadioSelect(),
        #            'marital_status': forms.RadioSelect(),
        #            'political_affiliation': forms.CheckboxSelectMultiple,
        #            'Smoker': forms.RadioSelect(),
        #            }
        labels = {
            "borrower_status": "Borrower Status. Check All That Apply.",
            "car": "Do You Own a Car?",
            "Pet": "Do You Own a Pet?",
            "social_media": "Social Media/ Tech Platform User? Check All That Apply.",
            "purchases": "Online Purchases. Check all that apply.",
            "news_sources": "Primary News Sources. Check all that apply.",
            "travel_frequency": "Vacation/Travel Frequency",
            "Kids": "How Many Kids Do You Have?",
        }

    def clean(self):
        cleaned_data = super(SurveyForm, self).clean()
        return cleaned_data
