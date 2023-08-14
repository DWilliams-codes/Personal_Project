from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Company
from .serializers import CompanySerializer

# Create your views here.
class All_Companies(APIView):
    def get(self, request):
        companies = CompanySerializer(Company.objects.all(), many = True)
        return Response(companies)
class A_Company(APIView):
    def get(self,request, name_or_id):
        if name_or_id.isnumeric():
            company = CompanySerializer(get_object_or_404(Company, id = name_or_id)).data
        else:
            company = CompanySerializer(get_object_or_404(Company, name = name_or_id)).data
        return Response(company)