from django.shortcuts import render
from .forms import  NewUserForm
from django.contrib.auth.models import User

# This view handles the landing page

from .models import UserModel, GameModel

def index(request):
    return render(request, 'gameApp/index.html',)


def newUser(request):
    form = NewUserForm(request.POST or None)
    context = {
        "new_form": form
    }

    if request.method == "POST":

        User.objects.create_user(request.POST["username"], "", request.POST["password1"])
        return render(request, "gameApp/creatuser.html", context)

    return render(request, 'gameApp/createuser.html', context)

#
# def edituser(request, id):
#     user= get_object_or_404(UserModel, pk = id)
#     edit_form = NewUserForm(request.POST or None, instance=user)
#     if edit_form.is_valid():
#         edit_form.save()
#         return redirect('index')
#
#     return render(request, 'gameApp/index.html', {'form': edit_form})
#
# def deleteuser(request, id):
#     user = get_object_or_404(UserModel, pk=id)
#     if request.method == 'POST':
#         user.delete()
#         return redirect('index')
#
#     return render(request, 'gameApp/index.html', {'selecteduser':user})
#
#

