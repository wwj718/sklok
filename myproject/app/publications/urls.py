#coding=utf-8
from views import show_all_book
from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('',
    url(r'^$',show_all_book),
)