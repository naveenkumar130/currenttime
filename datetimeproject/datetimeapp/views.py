from django.shortcuts import render
from django.http import HttpResponse
import datetime


# Create your views here.
def display(request):
    time=datetime.datetime.now()
    s='<h1>The Current Date and Time at Server is :'+str(time)+'</h1>'
    return HttpResponse(s)
