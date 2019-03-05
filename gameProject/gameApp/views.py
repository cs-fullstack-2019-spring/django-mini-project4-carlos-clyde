<<<<<<< HEAD
from django.shortcuts import render
from django.http import HttpResponse
from .models import UserModel,GameModel
from django.contrib.auth.models import User

=======
from django.shortcuts import render, redirect, get_object_or_404
>>>>>>> 8c76269801dffbb2bc1b665965c56ab44c89cc7f

# This view handles the landing page
from .forms import NewUserForm
from .models import UserModel, GameModel

def index(request):
<<<<<<< HEAD
    return HttpResponse("Hello, carlos")
    return render(request,'gameApp/index')
=======
    return render(request, 'gameApp/index.html',)

def createuser(request):
    new_form = NewUserForm(request.POST or None)
    if new_form.is_valid():
        new_form.save()
        return redirect('index')

    return render(request, 'gameApp/index.html', {'userform': new_form})

def edituser(request, id):
    user= get_object_or_404(UserModel, pk = id)
    edit_form = NewUserForm(request.POST or None, instance=user)
    if edit_form.is_valid():
        edit_form.save()
        return redirect('index')

    return render(request, 'gameApp/index.html', {'userform': edit_form})

def deleteuser(request, id):
    user = get_object_or_404(UserModel, pk=id)
    if request.method == 'POST':
        user.delete()
        return redirect('index')
>>>>>>> 8c76269801dffbb2bc1b665965c56ab44c89cc7f

    return render(request, 'gameApp/index.html', {'selecteduser':user})

<<<<<<< HEAD
def creatuser(request):
    return HttpResponse('hello, clyde')



=======
>>>>>>> 8c76269801dffbb2bc1b665965c56ab44c89cc7f
