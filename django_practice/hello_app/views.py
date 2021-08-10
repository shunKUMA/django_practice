from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def hello_appview(request):
    return HttpResponse('app is called')
