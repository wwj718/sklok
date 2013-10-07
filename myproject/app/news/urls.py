#coding=utf-8
from django.conf.urls.defaults import patterns, url
from models import News
from django.views.generic import date_based
from views import  get_by_id,search_by_title


news=News.objects.filter(categories='N').order_by('-id')
events=News.objects.filter(categories='E').order_by('-id')

news_info = {  
    "queryset"   : News.objects.all(),  
    "date_field" : "pub_date",
    'allow_empty': True, 
    'extra_context': {'news':news,'category':'N'}

} 

events_info = {  
    "queryset"   : News.objects.all(),  
    "date_field" : "pub_date",
    'allow_empty': True, 
    'extra_context': {'news':events,'category':'E'}

} 

#begin with /newsevents/
urlpatterns = patterns('',
    #(r'^$', date_based.archive_index, news_info), #默认页面
    (r'^categories/news/$', date_based.archive_index, news_info),  
    (r'^categories/events/$', date_based.archive_index, events_info),  
    (r'^categories/news/(?P<id>\d*)/$', get_by_id ),  
    (r'^categories/events/(?P<id>\d*)/$',get_by_id ),
    (r'^(?P<id>\d*)/$',get_by_id ),

    (r'^search/$',search_by_title),

)

