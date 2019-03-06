from django.shortcuts import render,redirect, get_object_or_404
from .forms import  NewUserForm,NewGameForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# This view handles the landing page

from .models import UserModel, GameModel
# this function was used as a tester to render the index page
def index(request):
    return render(request, 'gameApp/index.html',)
#function that creates a user


def newuser(request):
    # gets newUserForom and assigns it to form if the data is valid it will be posted to the database
    form = NewUserForm(request.POST or None)
    # passes in form and assigns to context new_form
    context = {
        "new_form": form
    }
    if request.method == "POST":
        # user created
        User.objects.create_user(request.POST["username"], "", request.POST["password1"])
        return render(request, "gameApp/addnewgame.html", context)
    return render(request, 'gameApp/createuser.html', context)

 # the game url form
def newgame(request):
    form = NewGameForm(request.POST or None)
    context = {
        "new_form": form
    }

    # if posted create a user name and password

    if request.method == "POST":
        # user created
        User.objects.create_user(request.POST["name"], "", request.POST["developer"])
        return render(request, "gameApp/addnewgame.html", context)

    return render(request, 'gameApp/addnewgame.html', context)
# gets the Game Form and assigns it to game_form if the data is valid it will be posted to the database
def newgameform(request):
    form = GameModel(request.POST or None)
    context = {
        'game_form': form
    }


    # if the request method equals a POST the index page is rendered

    if request.method == "POST":

        return render(request, "gameApp/index.html", context)

    return render(request, 'gameApp/index.html', context)

#when login link is clicked is directs user to the login html  page
def login(request):

    context = {
        'login': login
    }

    return render(request, 'registration/login.html', context)




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


