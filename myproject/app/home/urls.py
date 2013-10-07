#coding=utf-8
from views import  home
from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('',
    url(r'^$',home),
)