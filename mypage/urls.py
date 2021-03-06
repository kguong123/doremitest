"""hihi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from .views import *

urlpatterns = [
    url(r'^$', Mypage.as_view(), name='index'),
    url(r'^(?P<username>[-\w]+)/writelist/$', WriteLV, name='write_list'),
    url(r'^recipescrap/(?P<slug>[-\w]+)/$', RecipeSV, name='recipe_scrap'),
    url(r'^honeytipscrap/(?P<slug>[-\w]+)/$', HoneyTipSV, name='honeytip_scrap'),
    url(r'^(?P<username>[-\w]+)/scraplist/$', ScrapLV, name='scrap_list'),
    url(r'^userconfirm/$', DeleteConfirm.as_view(), name='user_confirm'),
    url(r'^userdelete/$', DeleteUser, name='user_delete'),
    url(r'^searchemail/$', SearchEmail.as_view(), name='search_email'),
    url(r'^findusername/$', FindUsername, name='find_username'),
    url(r'^searchpassword/$', SearchPassword.as_view(), name='search_password'),
    url(r'^findpassword/$', FindPassword, name='find_password'),
    url(r'^(?P<username>[-\w]+)/changepw/$', ChangePw, name='change_pw'),

]