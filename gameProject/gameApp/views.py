from django.shortcuts import render
from django.http import HttpResponse
from .models import UserModel,GameModel
from django.contrib.auth.models import User



def index(request):
    return HttpResponse("Hello, carlos")
    return render(request,'gameApp/index')


def creatuser(request):
    return HttpResponse('hello, clyde')



