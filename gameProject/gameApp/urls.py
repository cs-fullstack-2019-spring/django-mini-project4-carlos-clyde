from django.urls import path
from . import views



urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('createuser/', views.newUser, name='newUser'),
    path('addgame/',views.newgame, name='newgame')
]

