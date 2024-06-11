from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def lego_blog(request):
    return HttpResponse("Lets share Lego!")
