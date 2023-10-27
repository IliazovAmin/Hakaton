from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.


def index(request):
    return render(request, 'chat/index.html')

def base(request):
    return render(request, 'chat/base.html')

def floor(request):

    return render(request, 'chat/floor.html',)

def floor2(request):
    return render(request, 'chat/floor2.html')

def floor3(request):
    return render(request, 'chat/floor3.html')

def my (request):
    return render(request, 'chat/my.html')
