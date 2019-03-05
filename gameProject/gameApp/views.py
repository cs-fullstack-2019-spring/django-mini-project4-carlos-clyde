from django.shortcuts import render,redirect, get_object_or_404
from .forms import  NewUserForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# This view handles the landing page

from .models import UserModel, GameModel
# this function was used as a tester to render the index page
def index(request):
    return render(request, 'gameApp/index.html',)
#
def createuser(request):
    new_form = NewUserForm(request.POST or None)
    if new_form.is_valid():
        new_form.save()
        return redirect('index')

def newUser(request):
    form = NewUserForm(request.POST or None)
    context = {
        "new_form": form
    }

    if request.method == "POST":

        User.objects.create_user(request.POST["username"], "", request.POST["password1"])
        return render(request, "gameApp/createuser.html", context)

    return render(request, 'gameApp/createuser.html', context)

def newgameform(request):
    form = GameModel(request.POST or None)
    context = {
        'game_form': form
    }

    if request.method == "POST":

        return render(request, "gameApp/index.html", context)

    return render(request, 'gameApp/index.html', context)


def login(request):
    return render(request, 'gameApp/login.html')







def editgame(request, id):
    game_key= get_object_or_404(UserModel, pk = id)
    edit_form = NewUserForm(request.POST or None, instance=game_key)
    if edit_form.is_valid():
        edit_form.save()
        return redirect('index')

    return render(request, 'gameApp/index.html', {'form': edit_form})

def deletegame(request, id):
    game_key = get_object_or_404(UserModel, pk=id)
    if request.method == 'POST':
        game_key.delete()
        return redirect('index')

    return render(request, 'gameApp/index.html', {'selecteduser':game_key})



