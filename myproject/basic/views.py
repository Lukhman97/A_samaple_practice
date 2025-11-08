from django.shortcuts import render

# Create your views here.
from django.http import  HttpRequest,HttpResponse

def helath(request):
    return HttpResponse("I am lukhman shaik")