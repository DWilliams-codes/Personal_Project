from django.shortcuts import render
import requests
from rest_framework.views import APIView
from rest_framework.response import Response
import pprint
from datetime import datetime
from personal_project_env.api_keys import api_key, app_id
from job_posting_app.models import Job_Posting
from job_posting_app.serializers import Job_PostingSerializer
# Create your views here.
# Nice job hiding your API key on the front-end, but you'll likely still want to regenerate it along with the app_id if possible since it is still in the commit history for this PR.
# Ask about best way to intergrate data from Adzuna APIs
# Refactor to Grab Multiple Pages of Data
pp = pprint.PrettyPrinter(indent=2)
# I would break this function up a bit and follow the Single Responsibility Principle to isolate behavior and help debugging later on in your projects life
class Adzuna(APIView):
    def get_jobs(parameters=" "):
        try:
            # API Call
            endpoint = f"https://api.adzuna.com/v1/api/jobs/us/search/1?app_id={app_id}&app_key={api_key}{parameters}&results_per_page=50"
            response = requests.get(endpoint)
            jsonresponse = response.json()
            # API Serializer?
            job_list = []
            # Number of Jobs on the Returned page
            total = round(len(jsonresponse.get("results"))/2)
            # print(total)
            # loops through all the jobs on the page
            for jobs_num in range(total):
                id = jsonresponse.get("results")[jobs_num]["id"]
                title = jsonresponse.get("results")[jobs_num]["title"]
                description = jsonresponse.get("results")[jobs_num]["description"]
                salary = jsonresponse.get("results")[jobs_num]["salary_max"]
                location = jsonresponse.get("results")[jobs_num]["location"]["display_name"]
                # city = location.split(",")[0]
                company = jsonresponse.get("results")[jobs_num]["company"]["display_name"]
                recruiter = "Adzuna" # Adzuna doesn't have specific recruiters so all jobs will be given this default
                # Grab copy from local database or create posting, so it can be moved around in backend 
                # get or create job posting
                job_dict = {"id":id,"title":title,"job_description":description,"salary":salary,"location":location,"company":company,"recruiter":recruiter}
                # job_dict = Job_PostingSerializer(Job_Posting.objects.get_or_create(id=id,title=title,description=description,salary=salary,location=location,company=company,recruiter=recruiter), many = True).data
                # job_posting_object = Job_PostingSerializer(Job_Posting.objects.get_or_create(job_dict)).data
                # print(job_posting_object)
                job_list.append(job_dict)
                # list of all Job postings in the current year
            return job_list
        except:
            return([])
    def get_companies(parameters=" "):
        pass