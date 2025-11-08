from django.shortcuts import render

# Create your views here.
from django.http import  HttpRequest,HttpResponse

def health(request):
    return HttpResponse("I am lukhman shaik")

def lukh(request):
    return HttpResponse("Lukhman shaik786")