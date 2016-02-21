from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import CbObjects


def index(request):
    return HttpResponse("Hello, world. You're at the \"Startup Finder\" index.")

def detail(request, normalized_name):
    return HttpResponse("You're looking at company %s." % normalized_name)

def results(request, normalized_name):	
    response = "You're looking at the results of company %s."
    return HttpResponse(response % normalized_name)
