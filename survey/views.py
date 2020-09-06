from django.shortcuts import render
from survey.forms import *
from survey.models import *


def survey(request):5th commit
    if request.method == 'GET':
        surveyform = SurveyForm()
        return render(request, 'survey.html', locals())
    elif request.method == 'POST':
        form = SurveyForm(request.POST)
        print(form.__dict__)
        if form.is_valid():
            Profile_Name = form.cleaned_data['Profile_Name']
            borrower_status = form.cleaned_data['borrower_status']
            gender = form.cleaned_data['gender']
            age = form.cleaned_data['age']
            current_residence = form.cleaned_data['current_residence']
            education = form.cleaned_data['education']
            car = form.cleaned_data['car']
            household_income = form.cleaned_data['household_income']
            daily_internet_usage = form.cleaned_data['daily_internet_usage']
            Pet = form.cleaned_data['Pet']
            employment_status = form.cleaned_data['employment_status']
            employment_industry = form.cleaned_data['employment_industry']
            exercise = form.cleaned_data['exercise']
            social_media = form.cleaned_data['social_media']
            Purchases = form.cleaned_data['Purchases']
            news_sources = form.cleaned_data['news_sources']
            travel_frequency = form.cleaned_data['travel_frequency']
            marital_status = form.cleaned_data['marital_status']
            political_affiliation = form.cleaned_data['political_affiliation']
            Kids = form.cleaned_data['Kids']
            Smoker = form.cleaned_data['Smoker']
            submit_survey = Survey.objects.create(Profile_Name=Profile_Name, borrower_status=borrower_status,
                                                  gender=gender,
                                                  age=age, current_residence=current_residence, education=education,
                                                  car=car, household_income=household_income,
                                                  daily_internet_usage=daily_internet_usage,
                                                  Pet=Pet, employment_status=employment_status,
                                                  employment_industry=employment_industry,
                                                  exercise=exercise, social_media=social_media, Purchases=Purchases,
                                                  news_sources=news_sources, travel_frequency=travel_frequency,
                                                  marital_status=marital_status,
                                                  political_affiliation=political_affiliation,
                                                  Kids=Kids, Smoker=Smoker)
            submit_survey.save()
            message = '" {} " survey is submitted successfully'.format(Profile_Name)
            # message = 'survey is submitted successfully'
            form = SurveyForm()
            return render(request, "survey.html", {'message': message, 'surveyform': form})
        else:
            message = 'Please correct the below mentioned errors'
            return render(request, "survey.html", {'message': message, 'surveyform': form})
