from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    result = 'helllloo!oo!!'
    return HttpResponse(result, content_type="text/plain")

def taskstring(request):
    result = 'Rest API string!'
    return HttpResponse(result, content_type="text/plain")
