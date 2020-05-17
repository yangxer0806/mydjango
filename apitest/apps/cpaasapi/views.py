from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
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
        # return HttpResponse('username is ' + name)
        return render(request, 'index.html', context={'title':'测试平台','name' : name})