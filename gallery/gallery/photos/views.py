from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
'''started defining my functions'''
def welcome(request):
    return HTTPResponse('welcome to my gallery')