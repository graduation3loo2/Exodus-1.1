from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='Home'),
    path('vote', views.vote, name='Vote'),
    path('follow', views.follow, name='follow'),
    path('unFollow', views.un_follow, name='unFollow'),
]
