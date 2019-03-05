from django.shortcuts import render
from django.http import HttpResponse



def index(request):
    return HttpResponse("Hello, carlos")


def creatuser(request):
    return HttpResponse('hello, clyde')