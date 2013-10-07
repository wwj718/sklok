#coding=utf-8
from views import  show_all_facilities,get_by_category
from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('',
    url(r'^$',show_all_facilities),
    url(r'^categories/(?P<category>\w*)$',get_by_category)
)