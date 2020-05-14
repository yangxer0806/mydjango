from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request

# Create your views here.
def index(request):
    return HttpResponse('Hello World')

def login(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        return HttpResponse('Hello ' + name)
    else:
        if request.GET.get('name'):
            name = request.GET.get('name')
        else:
            name = 'EveryOne'
        return HttpResponse('username is ' + name)