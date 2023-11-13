"""
URL configuration for doobo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views
app_name='doobo'
urlpatterns = [
    path('',views.index,name='index'),
    path('<int:player_id>',views.detail,name='detail'),
    path('reply/create/<int:player_id>/', views.reply_create, name='reply_create'),
    path('reply/modify/<int:reply_id>/', views.reply_modify, name='reply_modify'),
    path('reply/delete/<int:reply_id>/', views.reply_delete, name='reply_delete'),
    path('player/voteu/<int:player_id>/',views.player_voteu, name='player_voteu'),
    path('player/voted/<int:player_id>/',views.player_voted, name='player_voted'),
    path('player/rvoteu/<int:reply_id>/',views.reply_voteu, name='reply_voteu'),
    path('player/rvoted/<int:reply_id>/',views.reply_voted, name='reply_voted'),
    path('add/pitcher', views.pitcher_add, name='pitcher_add'),
    path('add/batter', views.batter_add, name='batter_add'),
]
